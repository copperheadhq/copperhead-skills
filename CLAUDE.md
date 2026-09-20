# CLAUDE.md

## What this is

A collection of Claude Code agent skills, one folder per skill under
[skills/](skills/). [install.sh](install.sh) symlinks them into
`~/.claude/skills/` so the repo is the single source of truth — a skill is never
copied, so there is no second version to drift.

## Layout

```
skills/<name>/SKILL.md      required; frontmatter (name, description) + body
skills/<name>/references/   optional; loaded on demand
skills/<name>/scripts/      optional; executable helpers the skill invokes
skills/<name>/assets/       optional; templates and files used in output
```

## Rules that matter

**The description field is the trigger.** Claude reads it every turn and decides
from it alone whether to open the skill. It under-triggers by default, so
descriptions should be explicit and a little pushy: name the phrasings a user
would really type, and name where the skill should stay out of the way.

**`SKILL.md` loads in full when the skill fires.** Keep it under ~500 lines.
Long lists, lookup tables and worked examples go in `references/`, with a pointer
in the body saying when to read them. That's the progressive-disclosure split and
it's the main thing that keeps a skill cheap to have installed.

**Explain the why, don't stack MUSTs.** A skill that says "always do X" gets
followed literally in the cases it didn't anticipate. A skill that says why X
matters gets applied with judgement. Prefer the second.

**Editing a skill here is live.** The symlink means the next Claude Code turn
picks up the change. There is nothing to reinstall, and no build step.

## After changing a skill

Run `./install.sh --list` to confirm the link still resolves. If you rename a
skill folder, the old symlink in `~/.claude/skills/` goes stale — delete it by
hand and rerun `./install.sh`.
