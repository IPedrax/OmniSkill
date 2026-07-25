---
name: launch-runbook
description: Go-live and DNS cutover runbook. OmniSkill Operations crew — a time-ordered plan where every step names its verification and its rollback.
disable-model-invocation: true
---

# Launch Runbook

> Go-live + DNS cutover · OmniSkill Operations crew

## The rule

**Every step names how to verify it worked and how to undo it.** A runbook without rollback is a wish. At 2am, under pressure, with users affected, nobody invents a rollback procedure — they either have one or they improvise badly.

## Structure

```
Launch name · Date and time (with timezone) · Duration estimate
Roles: launch lead · technical owner · comms owner · approver
Communication channel and escalation path
Go / no-go criteria
Pre-launch checklist    (T-minus)
Cutover steps           (T-0, time-ordered)
Verification
Rollback procedure
Post-launch monitoring
```

Name a **single launch lead** with authority to call the rollback. Rollback decisions made by committee take too long, and the delay is where the real damage happens.

## Pre-launch (T-7 to T-1)

- Staging verified against production-like data
- Backups taken **and a restore actually tested**. An untested backup is not a backup.
- Database migrations rehearsed on a production-sized copy, with timing measured
- Rollback procedure written **and rehearsed**
- Monitoring and alerting in place for the new components *before* they carry traffic
- Capacity checked against expected load
- Dependencies confirmed: third-party services, certificates, credentials
- Support team briefed; internal comms drafted (see `/omniskill:internal-comms`)
- Go/no-go criteria agreed in writing, before the day

Set go/no-go criteria in advance, while nobody is under pressure. In the moment, sunk cost pushes everyone toward proceeding.

## DNS cutover

DNS is the step that most often goes wrong, because its effects are delayed and partly outside your control.

**Lower the TTL first.** At least 24–48 hours before cutover, reduce the record TTL to 300 seconds or less. TTL changes must themselves propagate at the *old* TTL — dropping it on the day achieves nothing.

Then:
1. Confirm the new infrastructure serves correctly when addressed directly, before any DNS change
2. Verify TLS certificates cover every hostname, and check the expiry dates
3. Make the DNS change
4. Verify from multiple resolvers and geographies, not just your own machine — your local cache is the least representative view available
5. **Keep the old infrastructure running** until traffic has fully drained. Propagation is not instant and some resolvers ignore TTL.
6. Watch both old and new for traffic and errors
7. Restore the normal TTL once stable

**Plan for split-brain.** During propagation, some users hit the old system and some the new. If both write to the same database this is usually fine; if each has its own, decide in advance how divergence is reconciled — or make the old one read-only for the window.

## Database migrations

Prefer **expand/contract**: add the new column or table, backfill, deploy code that writes both and reads new, then remove the old in a later release. This keeps every intermediate state rollback-safe.

A migration that drops or renames a column in the same deploy as the code change cannot be rolled back, because the old code no longer has the schema it needs. Long-running migrations should be run outside the cutover window.

## Verification

Not "the site loads". Check the paths that matter: signup, login, checkout, the core workflow, and any integration that touches money. Verify from an external network, on mobile, and as a logged-out user.

Watch error rates, latency, and queue depth against the pre-launch baseline — you need the baseline recorded beforehand to have anything to compare against.

## Rollback

Written before launch, with **decision criteria stated in advance**: what error rate, what latency, what duration triggers it. Deciding these in the moment guarantees a slow decision.

Document the exact steps, who executes, expected duration, and what data written since cutover must be preserved or reconciled. Rehearse it.

## Post-launch

Heightened monitoring for 24–48 hours. Someone on call who knows what changed. A scheduled check-in at 24 hours before declaring done. A short retrospective afterwards — route anything that went wrong to `/omniskill:incident-postmortem`.

## Checks before delivering

- Every step has verification and rollback.
- Rollback rehearsed, not just written.
- Backup restore tested.
- DNS TTL lowered 24–48h in advance.
- Certificates verified for all hostnames.
- Go/no-go and rollback criteria agreed in writing beforehand.
- A single named person can call the rollback.
- Baseline metrics recorded before cutover.
