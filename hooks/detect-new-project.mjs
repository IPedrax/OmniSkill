#!/usr/bin/env node
// OmniSkill new-project detector.
//
// Reads a Claude Code hook payload on stdin and, when it looks like a new
// project is starting, injects a suggestion telling Claude to OFFER the
// OmniSkill workforce via AskUserQuestion.
//
// It only ever injects text. It cannot activate anything, and it never blocks
// a prompt: any failure path exits 0 with no output.

import { readFileSync, existsSync, mkdirSync, readdirSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { tmpdir } from 'node:os';

const SUGGESTION =
  'The user may be starting a new project. Before doing the work, use AskUserQuestion to offer the ' +
  'OmniSkill workforce (54 skills across 7 departments: dev, design, marketing, social, finance, ops, legal). ' +
  'Name the specific department(s) that fit this request and why. Offer three choices: bring in the recommended ' +
  'crew, see all 7 departments first, or skip and continue normally. ' +
  'Do NOT load or act on any OmniSkill skill until the user picks. If they decline, drop it and do not ask again ' +
  'this session. If the request turns out not to be a new project, ignore this note entirely and proceed normally.';

// Intent patterns. Deliberately narrow — a false positive costs the user an
// interruption, so require language that implies building something new.
const INTENT = [
  /\b(build|create|make|start|set ?up|scaffold|bootstrap|spin ?up)\b[^.!?]{0,40}\b(new |a |an |me a |my )/i,
  /\bnew (project|app|application|site|website|repo|repository|service|product|business|startup|saas)\b/i,
  /\bfrom scratch\b/i,
  /\bgreen ?field\b/i,
  /\b(i want|i'?d like|help me|let'?s) (to )?(build|create|make|start|launch)\b/i,
  /\blaunch (a|my|our) (new )?(product|site|app|business|saas)\b/i,
];

// Things that mean "working in an existing codebase" — these veto a match.
const VETO = [
  /\b(fix|debug|refactor|rename|revert|typo|failing test|stack ?trace|error message)\b/i,
  /\b(this (bug|error|test|file|function|line))\b/i,
];

// Files that mean a real project already lives here.
const PROJECT_MARKERS = [
  '.git', 'package.json', 'pyproject.toml', 'Cargo.toml', 'go.mod', 'pom.xml',
  'build.gradle', 'Gemfile', 'composer.json', 'CMakeLists.txt', '*.csproj', '*.sln',
];

function isGreenfield(cwd) {
  try {
    const entries = readdirSync(cwd);
    const hasMarker = entries.some(
      (e) => PROJECT_MARKERS.includes(e) || /\.(csproj|sln)$/.test(e),
    );
    if (hasMarker) return false;
    // No manifest AND essentially nothing here. A directory full of files but
    // lacking a recognised manifest (docs, assets, a plugin like this one) is
    // still not a greenfield start.
    return entries.filter((e) => !e.startsWith('.')).length <= 2;
  } catch {
    return false; // unreadable cwd is not evidence of anything
  }
}

// Fire at most once per session. CLAUDE_PLUGIN_DATA survives plugin updates but
// does not exist before ~v2.1.2xx, so the OS temp dir is the working default on
// the 2.1.71 baseline. Session flags are disposable either way.
function alreadyOffered(sessionId) {
  if (!sessionId) return false;
  const dir = join(process.env.CLAUDE_PLUGIN_DATA || tmpdir(), 'omniskill-offers');
  const safe = String(sessionId).replace(/[^A-Za-z0-9_-]/g, '').slice(0, 128) || 'unknown';
  const flag = join(dir, `${safe}.flag`);
  try {
    if (existsSync(flag)) return true;
    mkdirSync(dir, { recursive: true });
    writeFileSync(flag, new Date().toISOString(), 'utf8');
    return false;
  } catch {
    return false; // never let bookkeeping suppress the offer
  }
}

function emit(event) {
  process.stdout.write(
    JSON.stringify({
      hookSpecificOutput: { hookEventName: event, additionalContext: SUGGESTION },
    }),
  );
}

// Off switch. OMNISKILL_AUTO_SUGGEST works on every version; the
// CLAUDE_PLUGIN_OPTION_* form is what Claude Code exports from a plugin
// userConfig toggle, which needs a newer build than the 2.1.71 baseline.
// Reading both means the /plugin toggle starts working on upgrade with no
// change here.
function enabled() {
  const v = (process.env.OMNISKILL_AUTO_SUGGEST ?? process.env.CLAUDE_PLUGIN_OPTION_AUTO_SUGGEST ?? '')
    .trim()
    .toLowerCase();
  return !['false', 'no', 'off', '0'].includes(v);
}

function run(payload) {
  if (!enabled()) return;

  const event = payload.hook_event_name || 'UserPromptSubmit';
  const cwd = payload.cwd || process.cwd();

  if (event === 'SessionStart') {
    // No prompt to read yet — an empty working directory is the only signal.
    if (isGreenfield(cwd) && !alreadyOffered(payload.session_id)) emit('SessionStart');
    return;
  }

  const prompt = payload.prompt || payload.user_prompt || '';
  if (!prompt || prompt.length > 4000) return;
  if (VETO.some((re) => re.test(prompt))) return;
  if (!INTENT.some((re) => re.test(prompt))) return;

  // Strong wording alone is enough; otherwise require a greenfield directory,
  // so "build me a login form" inside a real repo stays quiet.
  const explicit = /\bnew (project|app|application|site|website|repo|repository|product|saas)\b|\bfrom scratch\b/i.test(prompt);
  if (!explicit && !isGreenfield(cwd)) return;

  if (alreadyOffered(payload.session_id)) return;
  emit('UserPromptSubmit');
}

function selftest() {
  let failed = 0;
  const check = (label, actual, expected) => {
    const ok = actual === expected;
    if (!ok) failed++;
    console.log(`${ok ? 'ok  ' : 'FAIL'}  ${label}`);
  };

  const fired = (prompt, cwd = tmpdir()) => {
    const out = [];
    const realWrite = process.stdout.write.bind(process.stdout);
    process.stdout.write = (s) => { out.push(s); return true; };
    try {
      run({ hook_event_name: 'UserPromptSubmit', prompt, cwd, session_id: null });
    } finally {
      process.stdout.write = realWrite;
    }
    return out.join('');
  };

  // Positive: explicit new-project wording fires regardless of directory.
  check('explicit "new project" fires', fired('start a new project for invoicing') !== '', true);
  check('"from scratch" fires', fired('build me a SaaS landing page from scratch') !== '', true);
  check('"new app" fires', fired('I want to build a new app for tracking runs') !== '', true);

  // Negative: existing-codebase work stays quiet.
  check('typo fix silent', fired('fix this typo in the README') === '', true);
  check('debug silent', fired('debug this failing test') === '', true);
  check('refactor silent', fired('refactor this function to be smaller') === '', true);
  // Non-explicit build request in a directory that already has a project.
  check('vague build in real repo silent', fired('build me a login form', process.cwd()) === '', true);

  // Output shape.
  const payload = JSON.parse(fired('create a new website from scratch'));
  check('emits additionalContext', typeof payload.hookSpecificOutput.additionalContext === 'string', true);
  check('names the event', payload.hookSpecificOutput.hookEventName, 'UserPromptSubmit');

  // Dedupe: same session id fires once.
  const dedupeId = `selftest-${process.pid}`;
  const twice = () => {
    const out = [];
    const realWrite = process.stdout.write.bind(process.stdout);
    process.stdout.write = (s) => { out.push(s); return true; };
    try {
      run({ hook_event_name: 'UserPromptSubmit', prompt: 'start a new project', cwd: tmpdir(), session_id: dedupeId });
    } finally {
      process.stdout.write = realWrite;
    }
    return out.join('');
  };
  check('dedupe: first fires', twice() !== '', true);
  check('dedupe: second silent', twice() === '', true);

  console.log(failed === 0 ? '\nAll checks passed.' : `\n${failed} check(s) failed.`);
  process.exit(failed === 0 ? 0 : 1);
}

if (process.argv.includes('--selftest')) selftest();

// A broken detector must never block a prompt: swallow everything and exit 0.
try {
  const raw = readFileSync(0, 'utf8');
  if (raw.trim()) run(JSON.parse(raw));
} catch {
  // intentionally silent
}
process.exit(0);
