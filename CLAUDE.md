# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Course materials for two Occidental College Spring 2026 courses:
- `DL/` — COMP 395-2: Deep Learning
- `AILT/` — COMP 395-1: AI Learning Technologies

This is NOT a software project — there are no build/test/lint commands. The repo stores assignment files (PDFs, Jupyter notebooks) and context documents used to generate new assignments.

## Key Files

Each course directory has a `<course>.md` file (e.g., `DL/DL.md`, `AILT/AILT.md`) that serves as the **context prompt** for generating new assignments. These files contain:
- Course overview, student profile, pedagogical approach
- Prior assignment summaries (cumulative)
- Skills learned thus far (cumulative)
- Assignment request template (user fills in to request a new assignment)

Assignment files (`.ipynb`, `.pdf`) live alongside the `.md` file in each course directory.

## On every conversation start ("init")

1. **Check for new assignments:** Look at all PDFs and `.ipynb` files in each course directory. Compare them against the "Prior Assignments" section in the corresponding `.md` file. If any assignments exist as files but are not listed in the `.md`, read them and add a summary to the "Prior Assignments" section following the existing format.

2. **Update skills and concepts:** After adding any new assignments, review the new material and update the "Skills Learned Thus Far" section with any new skills, tools, concepts, or techniques that students gained from the new assignments. Integrate them into existing bullet points where appropriate, and add new bullets for genuinely new skill areas.

3. **Report what changed:** Tell the user what was added or confirm everything is up to date.

## Assignment Generation Guidelines

When generating assignments, follow these rules from the course `.md` files:

- **Pedagogy:** Cognitivist/constructivist approach — include think-pair-share activities, metacognition prompts, schema building, scaffolding. Critique each lesson like a learning scientist.
- **DL course pattern:** From-scratch implementation before PyTorch abstractions. Each assignment builds explicitly on prior skills (reference them).
- **Beamer slides:** No line numbers on code blocks. Use `upquote` package for straight ASCII quotes that copy correctly.
- **AI policy:** Students may use LLMs for boilerplate/debugging but must include transcripts and explain code verbally.
- **Assignment summaries:** When adding to "Prior Assignments", match the detail level and format of existing entries — include specific tools, datasets, techniques, and pedagogical activities.
- **Skills updates:** Integrate new skills into existing bullet points where they fit; only add new bullets for genuinely new skill areas.
