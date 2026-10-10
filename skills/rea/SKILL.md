---
name: rea
description: Understand a shipped app without its source. OmniSkill Developers crew. Bundled copy of REA's skill for its MCP server, which inspects Electron/JavaScript bundles, .NET assemblies, websites, network captures, APKs, firmware and native binaries (with Ghidra), and returns evidence and limits with every claim, so a feature seen elsewhere can be explained and then rebuilt.
disable-model-invocation: true
---

# rea

> See a feature, learn how it works, build your own · OmniSkill Developers crew

[REA](https://github.com/morluto/rea) is an MCP server (`mcp__rea__*`) plus a CLI. Point it at something already built (an Electron app's `app.asar`, a web page, a `.dll`, an APK, a binary) and it reports how the thing is put together, with the evidence behind each conclusion and what it could not see.

## Use it

Read `${CLAUDE_SKILL_DIR}/vendor/SKILL.md` and follow it; its `references/` sit alongside. Two places where this setup overrides it:

**Never run `rea setup`.** It writes REA's own copy of this skill into `~/.claude/skills`, which would load on every session and sit next to this one. When the tools are missing, search for them first (they may be deferred), then register the server alone:

```bash
claude mcp add rea --scope user -e NODE_OPTIONS=--max-old-space-size=12288 \
  -e REA_BROWSER_EXECUTABLE=/usr/bin/chromium -- npx -y rea-agents@6.3.0 mcp
```

`npx -y rea-agents@6.3.0 doctor --client claude_code --json` should report the registration healthy. A wide `doctor` also flags "skill identity missing" because it looks for its own copy in `~/.claude/skills`; that is this setup working as intended, not drift to repair.

**Versions move together.** The vendored skill is the one shipped inside `rea-agents@6.3.0` and describes exactly its 139 tools. Upgrading means bumping the pin above and replacing `vendor/` from the new npm package in the same commit, never one without the other.

## What works on this machine

| Target | Status |
|---|---|
| Electron / JavaScript bundles (`app.asar`, extracted trees), .NET assemblies, HAR captures, process capture | Ready, nothing else needed |
| A live web page | REA attaches to a browser you started, it doesn't launch one: run `chromium --remote-debugging-port=9222`, open the page, then `list_browser_targets` |
| Native binaries (pseudocode, assembly, symbols) | Needs Ghidra: `sudo pacman -S ghidra` (742 MB; Java 21+ is already here), then add `-e GHIDRA_INSTALL_DIR=/opt/ghidra` to the registration |
| Android APKs | Needs JADX: `sudo pacman -S jadx` |
| Firmware | Needs Binwalk or Unblob |

Name the missing piece and ask before installing anything; upstream's rule is the same.

## Before you point it at something big

**One bundle can stall the whole run.** On Claude Desktop's `app.asar`, REA parsed 259 of 320 files and then hung on a single 323 KB minified renderer bundle: with Node's default heap it died out of memory, with 12 GB it ran 40 minutes into `RangeError: Set maximum size exceeded` (a V8 limit no heap setting moves), and alone in its folder it never finished either. Everything else was fine: the 257-file, 20 MB main process (`.vite/build`) took 96 seconds. So:

- Time-box every run (`timeout -s KILL 600` on the CLI) and watch the `rea_progress` lines on stderr. Progress stuck on one file for minutes means that file, not the app's size.
- Extract the asar (`npx @electron/asar extract app.asar out`) and analyze one folder at a time, leaving out the folder with the stuck file. Say which part was skipped and that its findings are missing.
- Keep the larger heap from the registration; for the CLI set `NODE_OPTIONS=--max-old-space-size=12288`. It helps big apps, just not that case.

**Output size.** The CLI returns the complete evidence record. On a small Vite project with its `node_modules` that was 411 MB of JSON. Never read CLI output whole. Prefer the MCP tools, which answer narrow questions; on the CLI, select fields with `--filter-output normalized_result.summary` (`--token-limit` is refused on structured output). Point either at the shipped bundle (`app.asar`, `dist/`) rather than a source tree full of dependencies.

## House rules

**Rebuild from understanding, not from their code.** The point is "how does this work, so I can build mine". Explain the mechanism from the evidence, then write an original implementation. Pasting decompiled or minified code into the user's product carries the other author's copyright with it.

**Authorized targets only.** Apps the user installed and is studying for interoperability or learning, their own builds, and their clients' software with permission are fine. Breaking licence checks, DRM or anti-cheat, or pulling secrets out of someone else's app, is not, whatever the framing.

**Captures hold credentials.** HAR files and process captures record cookies, tokens and passwords. Never paste them into the conversation or a report; describe the field instead.

## Where it sits in the crew

`scrapling` reads what a site shows; REA explains how a site or app is built (bundles, IPC, network calls). Once the mechanism is clear, `superpowers` plans the rebuild. For security findings in an app (a vulnerability, an exploit path, a CTF binary), REA is the tool and the `CyberSECC` skill is the method.

## Attribution

Vendored from the `rea-agents@6.3.0` npm package (`skills/reverse-engineer-anything`, skill version 34; source [morluto/rea](https://github.com/morluto/rea)), licensed **MIT**. License at `${CLAUDE_SKILL_DIR}/vendor/LICENSE`.
