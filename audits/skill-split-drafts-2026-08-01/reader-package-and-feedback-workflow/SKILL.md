---
name: reader-package-and-feedback-workflow
description: Use when preparing fiction reader packages, feedback forms, reader-site files, and feedback archival without changing manuscripts.
version: 0.1.0-draft
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [fiction, novel-production, draft-skill, skill-split]
    related_skills: [longform-fiction-series-drafting]
---

# Reader Package And Feedback Workflow

## Purpose

Prepare reader-facing packages and feedback workflows for fiction projects. This includes feedback forms, reader instructions, reader-site generation, chapter-title regression guards, and feedback archival. Deployment uses separate deployment skills and requires normal safety checks.

## When to Use

- Building a family/beta/supporter reader package.
- Creating or updating feedback forms.
- Generating static reader-site files from manuscripts.
- Archiving reader feedback into the canonical repo.
- Checking free/locked library packaging rules.

## Non-Triggers

Do not use for manuscript revision. Do not deploy to VPS from this skill alone. Do not make reader feedback automatically rewrite prose.

## Procedure

1. Identify the canonical manuscript source and reader-site/source repo.
2. Read existing project-native feedback templates before inventing new ones.
3. Preserve the desired reader tone: family/casual vs commercial/editorial vs beta/deep.
4. Generate reader-facing files without changing canonical manuscript prose.
5. Validate forms are interactive and submittable.
6. Validate chapter titles/IDs and avoid first-sentence-as-title regressions.
7. Archive feedback forms/submissions in the repo.
8. If deployment is needed, hand off to deployment workflow with explicit target and cache-busting.

## Feedback Rules

- Reader reports are evidence, not automatic edit instructions.
- Archive raw feedback before interpretation.
- Keep family-reader forms warm and simple.
- Use project-specific addresses/templates where already chosen.

## Pitfalls

- Monolithic reader pages so large novels become unreadable.
- Disabled/display-only forms.
- Wrong feedback email address.
- Browser cache hiding deployed changes.
- Reusing another project’s generic form when a native form exists.

## Verification Checklist

- [ ] Source manuscript path verified.
- [ ] Existing feedback templates checked.
- [ ] Forms writable/selectable/submittable.
- [ ] Chapter titles/IDs validated.
- [ ] No manuscript prose changed.
- [ ] Deployment, if any, handled separately with approval.
