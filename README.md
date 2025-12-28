# Raven

**Be Odin. Send ravens.**

Odin-Raven is a semantic CLI wrapper around Git.
It replaces mechanical Git commands with intent-driven verbs like `watch`, `gather`, and `fly`.

---

## Why Odin-Raven?

Git is powerful, but its commands are mechanical.
Odin-Raven adds a thin, human-friendly layer on top of Git without changing how Git works.

Git remains the engine.
Raven is the messenger.

---

## Installation

```bash
pip install odin-raven
```

After installation:

```bash
raven --help
```

---

## Core Workflow

```bash
raven watch
raven gather
raven mark "feat: add new feature"
raven fly
```

Equivalent Git commands:

```bash
git status
git add .
git commit -m "feat: add new feature"
git push
```

---

## Commands

| Raven Command          | Git Equivalent    | Meaning               |
| ---------------------- | ----------------- | --------------------- |
| `raven awaken`         | `git init`        | Initialize repository |
| `raven watch`          | `git status`      | Observe repo state    |
| `raven gather`         | `git add .`       | Stage changes         |
| `raven mark "msg"`     | `git commit -m`   | Record a commit       |
| `raven fly`            | `git push`        | Push changes          |
| `raven sync`           | `git pull`        | Sync with remote      |
| `raven huginn`         | `git diff`        | Think before acting   |
| `raven muninn`         | `git log`         | Recall history        |
| `raven paths`          | `git branch`      | View branches         |
| `raven perch <branch>` | `git checkout`    | Switch branch         |
| `raven spawn <branch>` | `git checkout -b` | Create branch         |
| `raven merge <branch>` | `git merge`       | Merge branch          |

---

## Mythology (Light Touch)

In Norse mythology, Odin sends two ravens:

- **Huginn** — Thought
- **Muninn** — Memory

They observe the world and report back.

This project borrows that idea:

- `huginn` → inspect changes
- `muninn` → inspect history

---

## Status

**v0.1.0**
Stable, simple, and complete.

Future additions may happen — or may not.

---

## License

MIT

---
