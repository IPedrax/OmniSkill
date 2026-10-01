---
name: airship
description: Visual editor for the running app. OmniSkill Design crew — drives the airship CLI, which puts an infinite canvas in front of the dev server you already have: click an element, describe the change, and a coding agent edits the source file it came from.
disable-model-invocation: true
---

# Airship

> Point at it instead of describing it · OmniSkill Design crew

The rest of this crew works in one direction: decide, then build. Airship closes the loop the other way. It runs a reverse proxy in front of the dev server that is already up, renders the app on a pannable canvas at several real device sizes at once, and turns a click into the file and line that drew it. Describe the change, and a coding agent edits the source.

That makes it the right tool for the last stretch of a design — the hundred small judgments about spacing, weight, and rhythm that are faster pointed at than written down.

Not bundled. It is a **CLI**, not skill content: [`@airshiplabs/cli`](https://www.npmjs.com/package/@airshiplabs/cli) runs from npm and adds nothing to the project's dependencies, config, or bundle.

## Launch it

```bash
npx @airshiplabs/cli --target 3000
```

`--target` is the port the dev server is already on; airship opens the editor on the next free port. Install it once with `npm i -g @airshiplabs/cli` and the binary is `airship`. Node 22.13 or later.

Bare `airship` asks for the port, the agent and the mode. `airship init` writes an `airship.config.json` so it stops asking. `airship doctor` checks node, config, git, the overlay bundle, each agent and the dev server, and exits `1` if anything failed — so `airship doctor && airship` is the safe form on a machine that has not run it before.

The flags worth deciding before launch, rather than after:

| Flag | Decide it when |
| --- | --- |
| `-t, --target <port>` | Always, unless the dev script makes the port obvious — detection falls back to guessing common ports. |
| `--cwd <dir>` | **Monorepo.** This is the folder the dev server treats as its root, which is where `/src/app.tsx` resolves from — `apps/web`, not the repository root. |
| `--exec "<cmd>"` | The dev server is not running yet and should stop when airship does. Then the port has to be *free*, not occupied. |
| `--safe` | The agent should be confined. Read [Safety](#safety) first — it is not equally strong on all three agents. |
| `--commit` | Auto-commits each accepted edit with a Conventional Commits message. Worth it: a visual session produces many small edits, and this is what keeps them reviewable one at a time. |
| `-a, --agent <name>` | `claude` (default), `codex`, `opencode`. |
| `--mode <name>` | `canvas` (default, one frame per device size) or `inline` (the editor over the real page). Switchable from the bottom bar. |

**Point it at the dev server, not a production preview.** The element-to-file mapping comes from the source locations dev builds record. Aim it at `vite preview` or `next start` and the canvas still renders, but a click no longer knows what wrote it.

## Agents

Airship spawns the agent itself, reusing the login that agent already has — `ANTHROPIC_API_KEY` or a `claude` login, `CODEX_API_KEY` / `OPENAI_API_KEY` or `codex login`, a provider key or `opencode auth login`. It warns at startup when it finds none.

Three differences actually change what to pick:

- **Undo is airship's, not the agent's.** It keeps the previous version of every file it touches. On `claude` it snapshots that itself; on `codex` and `opencode` it reconstructs the baseline from Git, so **those two need the project to be a repository** or undo silently has nothing to restore.
- **Only `codex` gets a real sandbox** under `--safe` — see below.
- **`opencode` is a separate install** (`brew install sst/tap/opencode` or `npm i -g opencode-ai`). `claude` and `codex` are included. It also needs the `provider/model` form for `--model`, and ignores `--effort`, `--max-turns` and `--max-budget`.

## Safety

**By default the agent runs unsandboxed** — the same access it has from a terminal. `--safe` narrows that, unequally:

| | `--safe` gives you |
| --- | --- |
| `codex` | A real OS sandbox: locked to the project folder, no network, no web search. |
| `claude` | Edits checked against the project directory, dangerous commands blocked. A check, not a wall. |
| `opencode` | Asks before every edit and command, same checking; no web fetch or search. |

The check catches known-dangerous commands. It does not understand shell, so it catches `rm -rf` and not `echo x > /elsewhere`, and on `claude` and `opencode` a command it allows can still open a network connection. If a hard guarantee matters more than which agent runs, that is `airship --agent codex --safe`.

**The editor is an unauthenticated local server that can drive an agent with write access.** It binds `127.0.0.1` for that reason. Widening it with `--host 0.0.0.0` — for Docker, or to open the canvas on a phone — means anything on that network can drive the agent, which is the same exposure as leaving a terminal unlocked. Behind a proxy or a hostname alias, name it in `--allowed-hosts`; airship never reads `X-Forwarded-Host`, and exact-match hostnames are what block DNS rebinding.

## House rules

**One agent in the tree at a time.** Airship runs its own agent process against the same files this session is editing, with a separate undo stack that knows nothing about edits made from here. Finish the current change and commit it before handing over, and treat the airship session as owning the working tree until the user closes it. Two agents editing the same component is not a merge conflict — it is a lost edit.

**Do not launch it from this session.** It is a long-running server whose whole interface is a canvas in a browser; there is nothing here to drive it with, and starting it in the background just puts a second writer on the repo unattended. Hand the user the exact command — target, `--cwd`, `--safe`, `--commit` — and let them run it in their own terminal.

**Recommend `--commit` on a real repository.** Undo covers the last edit; a commit per accepted change covers the session. Reviewing forty visual tweaks as one diff is how a good session ends up reverted whole.

**A blank frame means framing headers.** Airship strips `X-Frame-Options` and `frame-ancestors` from the surfaces it serves, so this only happens under `--keep-csp`. Drop the flag rather than loosening the app's real policy.

**It works with the styling system already in the project.** Tailwind, CSS Modules, styled-components — the change lands in the source file, so it should land in the same tokens and conventions the codebase already uses. If the project has a design spec from `anydesign` or `ui-ux-pro-max`, that spec still governs; the canvas is a faster way to hit it, not permission to freehand.

## Where it sits in the crew

After `frontend-design`, and alongside `motion-ui`. Direction from `anydesign` or `ui-ux-pro-max`, the interface from `frontend-design`, then airship for the iteration pass on the running thing — where a spacing scale that read fine in a spec turns out to be wrong at mobile width.

It is not a substitute for deciding direction. An infinite canvas over an undecided design produces a hundred fast, uncommitted adjustments, which is the templated look this crew exists to avoid, arrived at more quickly. Settle the spec first, then point at it.

## Attribution

[Airship](https://github.com/0xnyn/airship) by Nayan Kumar · [airship.design](https://airship.design) · **MIT**. Nothing is vendored here; the CLI installs from npm.
