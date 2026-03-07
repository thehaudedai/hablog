# Hablog

## List of Commands for V1

### Session Management

```bash
hablog start <project>              # Start a new session
hablog end                          # End the current session
hablog status                       # Show current active session
hablog restart <project>            # End current session (if any) and start a new one
```

### Breaks / Pauses

```bash
hablog break start                  # Start a break within a session
hablog break end                    # End the current break
hablog break status                 # Show active break info
```

### Stats/Reporting

```bash
hablog stats                          # Show stats for all time
hablog stats --today                  # Show stats for today
hablog stats --week                   # Show stats for this week
hablog stats --<project>              # Show stats for a specific project
```

### Optional Notes / Metadata

```bash
hablog start <project> --note "reading chapter 1"                      # Add a note to the session
hablog start <project> --tags "study,python"                           # Add tags to session
hablog end --note "finished half the chapter"                          # Add a note at session end
hablog restart <project> --note "Bored of Reading" --tags "study"      # Add a note and a tag when restarting new session
```

### Export / Utility (future)

```bash
hablog export --format json       # Export all sessions as JSON
hablog export --format csv        # Export all sessions as CSV
```

---

## Checklist

- [ ] start
- [ ] end
- [ ] restart
   - [ ] --note, --tags
- [ ] status

- [ ] break start
- [ ] break end
- [ ] break status

- [ ] stats
   - [ ] --today, --week, --<project>

- [ ] export
   - [ ] --format

---
