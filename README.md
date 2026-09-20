# copperhead-skills

Agent skills for Claude Code, kept in one place so they're versioned, reviewable
and shared across machines instead of living loose in `~/.claude/skills/`.

A skill is a folder with a `SKILL.md` in it. The frontmatter says when Claude
should reach for it, the body says what to do and anything under `references/`
loads only when it's actually needed. Claude reads the description on every turn
and pulls the rest in when the task matches.

## Skills

| Skill | What it does |
| --- | --- |
| [humanizer](skills/humanizer/) | Rewrites prose so it stops reading like a machine wrote it. Three passes: cut the stock vocabulary and the stock shapes, put the rhythm back, then add the small human moves that make a page feel written rather than generated. |

### Auditing a rewrite

The humanizer ships a checker. It reads the ban list out of `SKILL.md`, so the
rules and the tool can't drift apart.

```bash
python3 skills/humanizer/scripts/audit.py after.txt --before draft.txt
```

It reports word-count delta, sentence-length variation with a rhythm sparkline,
and counts for banned words, em dashes, serial commas, comma splices, trailing
-ing clauses and typographic artifacts. `--strict` exits nonzero when a hard
rule is still broken, which makes it usable in a commit hook. `--json` gives
the raw numbers and `-` reads stdin.

Pointing it at the skill's own files is not meaningful. `SKILL.md` contains the
ban list, so it reports every banned word as present.

## Install

```bash
git clone git@github.com:copperheadhq/copperhead-skills.git
cd copperhead-skills
./install.sh
```

That symlinks every skill into `~/.claude/skills/`. Symlinks and not copies, so
editing a skill here takes effect on the next Claude Code turn. No reinstall
step to forget.

Link one skill instead of all of them:

```bash
./install.sh humanizer
```

Check what's linked:

```bash
./install.sh --list
```

The script won't clobber a real directory that's already sitting at the
destination. It tells you to move it aside and skips it.

## Adding a skill

Make the folder, write the `SKILL.md`, run `./install.sh`.

```
skills/<name>/
├── SKILL.md          required: frontmatter + instructions
└── references/       optional: loaded on demand, not every turn
```

The frontmatter needs `name` and `description`:

```yaml
---
name: my-skill
description: What it does, then the contexts that should trigger it.
---
```

Two things worth getting right:

**The description is the whole triggering mechanism.** Claude decides whether to
open a skill from that one field. It under-triggers by default. List the
phrasings a user would actually type, including the ones that never name the
skill. Say where it shouldn't fire, too.

**Keep `SKILL.md` under about 500 lines.** It loads in full whenever the skill
fires. The long tables, the exhaustive lists and the worked examples belong in
`references/` with a line in the body saying when to go read them.

## License

Apache 2.0. See [LICENSE](LICENSE).
