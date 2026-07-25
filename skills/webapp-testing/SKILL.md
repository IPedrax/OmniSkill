---
name: webapp-testing
description: Browser-test a web app. OmniSkill Developers crew — drives a real browser to verify user flows, catches console and network errors, and writes tests that do not flake.
disable-model-invocation: true
---

# Webapp Testing

> Browser-tests your app · OmniSkill Developers crew

Verifying a web application works by driving a real browser — not by reading the code and concluding it should work.

## Pick the driver

Use whichever browser automation is available in the session:

- **Playwright MCP** (`mcp__playwright__*`) — `browser_navigate`, `browser_snapshot`, `browser_click`, `browser_fill_form`, `browser_console_messages`, `browser_network_requests`
- **Chrome DevTools MCP** (`mcp__chrome-devtools__*`) — adds `performance_start_trace` and `lighthouse_audit` for performance work
- **The in-app browser** (`mcp__Claude_Browser__*`) — `read_page` returns an accessibility tree with `ref_N` handles

Prefer the **accessibility snapshot over a screenshot** for verifying content and structure. It is faster, cheaper, deterministic, and gives stable element handles. Screenshots are for visual questions only.

## The flow

**1 — Get it running.** Start the dev server through the preview tooling rather than a raw shell command, so the process is managed and its logs are readable.

**2 — Snapshot before acting.** Read the page to get element references. Never click blind coordinates when refs are available — coordinate clicks break on any layout change.

**3 — Drive the real user path.** Not just page loads: sign up, log in, complete the core workflow, submit the form, check the result actually persisted.

**4 — Read the console and network.** This is the step most often skipped and the one that finds the most. A page can look correct while throwing errors, 404ing an asset, or firing a request that silently fails. Check both on every run.

**5 — Verify state actually changed.** Reload and confirm the change survived. A UI that updates optimistically and never persists looks identical to one that works.

## What to test

- **Happy path** end to end, for each core workflow
- **Validation** — submit empty, submit invalid, submit a duplicate
- **Auth boundaries** — logged out, wrong user, expired session. Confirm the *server* refuses, not just that the UI hides the button.
- **Error states** — what the user sees when a request fails
- **Empty states** — first run, no data. Frequently broken because it is rarely seen in development.
- **Mobile viewport** — resize and re-run the core flow
- **Keyboard navigation** — tab through the form, confirm focus is visible and order is sensible

## Writing tests that do not flake

Flaky tests get disabled, and disabled tests protect nothing.

- **Never sleep for a fixed duration.** Wait for a condition — an element, a network response, a text change. `sleep(2000)` is both slower and less reliable than waiting for the actual signal.
- **Select by role, label, or test id** — not by CSS class or DOM position. Class names change on every refactor.
- **Each test sets up its own data and cleans up.** Tests that depend on execution order fail the moment one is run alone.
- **No shared mutable state** between tests.
- **Assert on user-visible outcomes**, not implementation details.

## Debugging a failure

Read the console errors first, then the failed network requests, then the accessibility snapshot at the point of failure. Most failures are visible in one of those three and need no further instrumentation.

If a test passes alone but fails in the suite, the cause is shared state or ordering, not timing — adding a wait hides it rather than fixing it.

## Report honestly

State what was tested, what passed, what failed, and what was **not** covered. "Login and checkout verified; payment flow not tested because it needs live credentials" is a useful report. "Tests pass" is not, because it implies coverage that may not exist.

Never report a flow as working without having driven it.

## Checks before delivering

- The app was actually run and driven, not just read.
- Console and network checked on every flow.
- State persistence verified by reload.
- Error and empty states exercised.
- No fixed sleeps in any test written.
- Selectors are role-, label-, or test-id-based.
- Untested areas stated explicitly.
