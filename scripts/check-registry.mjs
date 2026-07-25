#!/usr/bin/env node
// Validates the OmniSkill tree against references/registry.md.
//
// Three invariants:
//   1. Every registry entry has a skill directory, and every skill directory is
//      in the registry.
//   2. Exactly 8 skills are model-invocable (router + 7 departments). This is the
//      context-budget invariant — the whole architecture rests on it.
//   3. Every SKILL.md has parseable frontmatter with a name and description.

import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const SKILLS = join(ROOT, 'skills');
const REGISTRY = join(ROOT, 'references', 'registry.md');

const ROUTERS = ['omniskill', 'dev', 'design', 'marketing', 'social-content', 'finance', 'ops', 'legal'];
const EXPECTED_LEAVES = 42;

const errors = [];
const warnings = [];

// --- parse the registry: leaf names live in the first column of the dept tables
const registryText = readFileSync(REGISTRY, 'utf8');
const registered = new Set();
for (const m of registryText.matchAll(/^\|\s*`([a-z0-9-]+)`\s*\|/gim)) registered.add(m[1]);

// --- walk the skills tree
const onDisk = readdirSync(SKILLS, { withFileTypes: true })
  .filter((d) => d.isDirectory())
  .map((d) => d.name);

const meta = new Map();
for (const name of onDisk) {
  const file = join(SKILLS, name, 'SKILL.md');
  if (!existsSync(file)) {
    errors.push(`${name}/ has no SKILL.md`);
    continue;
  }
  const text = readFileSync(file, 'utf8');
  const fm = text.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!fm) {
    errors.push(`${name}: no YAML frontmatter`);
    continue;
  }
  const body = fm[1];
  const field = (k) => (body.match(new RegExp(`^${k}:\\s*(.+)$`, 'm')) || [])[1]?.trim();

  const entry = {
    name: field('name'),
    description: field('description'),
    disabled: /^disable-model-invocation:\s*(true|yes|on|1)\s*$/im.test(body),
  };
  meta.set(name, entry);

  if (!entry.name) errors.push(`${name}: frontmatter missing 'name'`);
  else if (entry.name !== name) errors.push(`${name}: frontmatter name '${entry.name}' != directory name`);
  if (!entry.description) errors.push(`${name}: frontmatter missing 'description'`);
  else if (entry.description.length > 1024) {
    warnings.push(`${name}: description is ${entry.description.length} chars (listing caps at 1536 incl. when_to_use)`);
  }
}

// --- invariant 1: registry and disk agree
const leaves = onDisk.filter((n) => !ROUTERS.includes(n));
for (const name of registered) {
  if (!onDisk.includes(name)) errors.push(`registry lists '${name}' but skills/${name}/ does not exist`);
}
for (const name of leaves) {
  if (!registered.has(name)) errors.push(`skills/${name}/ exists but is not in the registry`);
}
if (leaves.length !== EXPECTED_LEAVES) {
  errors.push(`expected ${EXPECTED_LEAVES} leaf skills, found ${leaves.length}`);
}

// --- invariant 2: the context-budget guarantee
const invocable = [...meta.entries()].filter(([, m]) => !m.disabled).map(([n]) => n).sort();
if (invocable.length !== ROUTERS.length) {
  errors.push(
    `context budget: expected ${ROUTERS.length} model-invocable skills, found ${invocable.length}\n` +
      `    invocable: ${invocable.join(', ')}\n` +
      `    every leaf must set 'disable-model-invocation: true'`,
  );
}
for (const r of ROUTERS) {
  if (!onDisk.includes(r)) errors.push(`router skills/${r}/ is missing`);
  else if (meta.get(r)?.disabled) errors.push(`router '${r}' must NOT set disable-model-invocation`);
}

// --- report
console.log(`skills on disk : ${onDisk.length} (${ROUTERS.length} routers + ${leaves.length} leaves)`);
console.log(`registry entries: ${registered.size}`);
console.log(`model-invocable : ${invocable.length}  [${invocable.join(', ')}]`);

for (const w of warnings) console.log(`WARN  ${w}`);
if (errors.length) {
  console.error(`\n${errors.length} error(s):`);
  for (const e of errors) console.error(`  - ${e}`);
  process.exit(1);
}
console.log('\nAll checks passed.');
