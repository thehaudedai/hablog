# Hablog

**Hablog** is a lightweight CLI tool for tracking work sessions with minimal friction.
It is designed especially for people with **ADHD**, helping reduce decision fatigue by remembering where you left off and making it easy to resume work.

The tool focuses on two simple ideas:

- **Sessions** – short blocks of focused work
- **Projects** – areas of work that accumulate sessions and track progress

Sessions can be short (even 5 minutes). The goal is **momentum, not perfection**.

---

# Installation

_(Installation instructions will be added once packaging is ready.)_

---

# Core Concepts

## Sessions

A **session** is a block of time spent working on a project.

Sessions track:

- start time
- end time
- duration
- project
- optional tags

Even short sessions count toward progress.

---

## Projects

Projects represent areas of work (for example: `reading`, `coding`, `game-dev`).

Projects track:

- progress toward a **target number of sessions**
- current **status** (active, paused, done, abandoned)
- **tags** for categorization
- **next steps** so you remember what to do next time

This helps reduce the common ADHD problem of:

> "I want to work… but I don't know where to start."

---

# Commands (V1)

## Session Management

Start and stop work sessions.

```bash
hablog start <project>
hablog end
hablog restart <project>
hablog status
```

### Examples

```bash
hablog start reading
hablog end
hablog restart coding
```

**start**

- Starts a new session for the specified project.

**end**

- Ends the currently active session.

**restart**

- Ends the current session (if one exists) and immediately starts another.

**status**

- Shows the currently active session and how long it has been running.

---

## Project Management

Create and manage projects.

```bash
hablog create <project> --target <sessions> --status active --tags <tag1,tag2>
```

### Example

```bash
hablog create reading --target 30
```

Fields:

| Field   | Description                                             |
| ------- | ------------------------------------------------------- |
| project | project name                                            |
| target  | number of sessions to complete                          |
| status  | project state (`active`, `paused`, `done`, `abandoned`) |
| tags    | optional tags                                           |

---

## Viewing Data

```bash
hablog view
```

Displays logged sessions in a readable format.

---

# Future Features

These are planned but not part of the initial MVP.

### Statistics

```bash
hablog stats
hablog stats --today
hablog stats --week
hablog stats --project <project>
```

Will include:

- time spent per project
- sessions per day
- progress toward targets

---

## Editing Sessions

Fix mistakes if needed.

```bash
hablog edit <session-id> \
  --p <project> \
  --st <start-time> \
  --et <end-time> \
  --tags <tags>
```

Session ID cannot be modified.

---

### Export

```bash
hablog export --format json
hablog export --format csv
```

Export sessions for external analysis or visualization.

---

# Example Workflow

```bash
hablog create reading --target 30

hablog start reading
# work...

hablog end

hablog status
```

---

# Philosophy

Hablog is built around a few simple principles:

**1. Low friction**

- Commands should be quick and forgiving.

**2. Progress over perfection**

- Even small sessions count.

**3. Reduce decision fatigue**

- Projects remember where you left off.

**4. CLI-first**

- Simple, fast, scriptable.

---

# Project Status

This project is currently in **MVP development**.

Core functionality being implemented:

- session tracking
- project creation
- active session monitoring
- basic editing

More features will be added after the core workflow is stable.

---

# License

_(Exact license yet to be decided)_
