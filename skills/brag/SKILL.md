---
name: brag
description: A 20-second launch video of what you built. OmniSkill Social & Content crew. Bundled copy of brag-slim, which reads a project or a live URL, plans a hook-reveal-highlights-punchline storyboard, renders brag.mp4 from the product's own UI with a soundtrack it makes itself, and writes the share copy.
disable-model-invocation: true
---

# brag

> You built it. Now show it · OmniSkill Social & Content crew

**Bundled, nothing to install.** It builds the whole video with tools already on the machine: a headless browser to draw frames from the project's real components, and FFmpeg to encode them and mix the soundtrack.

## Use it

Read `${CLAUDE_SKILL_DIR}/vendor/SKILL.md` and follow it. Ignore its line about deferring to a separate `/brag` skill; that is upstream's own plugin, and this copy is the one to use. Outputs go to `brag-output/` in the user's current directory, never into the plugin folder.

Check the two tools before planning anything, because a storyboard nobody can render is wasted work: `ffmpeg -version`, and a Chromium for Playwright or Puppeteer (one is often already under `~/.cache/ms-playwright`). If either is missing, say which one and stop.

## Where it sits in the crew

Against `video`: that one scripts video for a person to shoot and edit, built around retention on a platform. `brag` renders the finished file itself, from the product's own interface, and it is for one moment: a launch, a release, a new feature. Use `video` for an ongoing channel and `brag` for the announcement.

It chains forward: `share-copy.txt` is a first draft, and `social` turns it into platform-native posts for wherever the video is going. When the product has no interface worth showing yet, Design comes first.

## House rules

**Only the product's own claims.** Upstream already bans invented numbers and testimonials. Hold that line when a tone preset like `yc-parody` or `cinematic` invites a big claim: the joke can be in the delivery, never in a fake metric.

**Make the music, don't fetch it.** The soundtrack must be generated on the machine or come from a source the user names with its license. Pulling a recognisable track from the web is the fastest way to get a launch video muted or taken down.

**A client's project is the client's to post.** When the code belongs to a freelance client, the video is a draft for them to approve, not something to publish from the user's own accounts.

## Attribution

Vendored from [latent-spaces/brag](https://github.com/latent-spaces/brag) @ `d06a77f`: `skills/brag-slim` only, licensed **MIT**. License at `${CLAUDE_SKILL_DIR}/vendor/LICENSE`. The full `/brag` is not included: it depends on the Hyperframes CLI and bundles five ende.app music tracks whose redistribution terms upstream itself says are unverified.
