# Skill Creator Guide

Reference for creating high-quality Claude Code skills.

## Table of Contents
1. [Skill Structure](#skill-structure)
2. [YAML Frontmatter](#yaml-frontmatter)
3. [Context Efficiency](#context-efficiency)
4. [Progressive Disclosure](#progressive-disclosure)
5. [Writing Guidelines](#writing-guidelines)
6. [Common Patterns](#common-patterns)

---

## Skill Structure

Every skill requires at minimum:

```
skill-name/
├── SKILL.md          # Required: Main instructions
├── references/       # Optional: Detailed documentation
│   ├── topic-1.md
│   └── topic-2.md
├── scripts/          # Optional: Executable code
│   └── helper.ts
└── assets/           # Optional: Templates, boilerplate
    └── template.ts
```

### SKILL.md (Required)
- YAML frontmatter with `name` and `description`
- Markdown body with instructions
- **Keep under 500 lines** - split into references if larger

### references/ (Optional)
- Detailed documentation loaded on demand
- One topic per file
- Reference from SKILL.md: "See `references/api.md` for details"

### scripts/ (Optional)
- Executable code for deterministic tasks
- Claude can run these via Bash tool
- Use for: API calls, file processing, validation

### assets/ (Optional)
- Code templates and boilerplate
- Claude reads and adapts these for user's needs
- Use for: starter code, config files, type definitions

---

## YAML Frontmatter

Required fields:

```yaml
---
name: skill-name
description: One-line description of what this skill does
---
```

Optional fields:

```yaml
---
name: skill-name
description: One-line description
version: 1.0.0
author: Your Name
tags: [category1, category2]
---
```

### Writing Good Descriptions

**Good descriptions** are specific and action-oriented:
- "Generate Playwright browser automation scripts with Browserbase infrastructure"
- "Create and manage Stripe payment integrations with proper error handling"
- "Build Next.js API routes following App Router conventions"

**Bad descriptions** are vague:
- "Help with browser stuff"
- "Stripe helper"
- "Next.js skill"

---

## Context Efficiency

> "The context window is a public good."

Every token in SKILL.md costs context space. Only include information that:
1. Claude cannot deduce from general knowledge
2. Is specific to this tool/library
3. Users will need frequently

### What to Include
- Specific API patterns unique to this tool
- Common gotchas and their solutions
- Code templates for frequent tasks
- Trigger keywords/phrases

### What to Exclude
- General programming concepts
- Information Claude already knows
- Rarely-used features (put in references/)
- Verbose explanations (show code instead)

### Example: Good vs Bad

**Bad** (verbose, states the obvious):
```markdown
## Installation

To install this package, you need to use npm, which is the Node Package
Manager. npm comes bundled with Node.js. First, make sure you have Node.js
installed on your system. You can check this by running `node --version`
in your terminal. Once you've confirmed Node.js is installed, you can
install the package by running the following command:

npm install example-package
```

**Good** (concise, actionable):
```markdown
## Installation

npm install example-package
```

---

## Progressive Disclosure

Skills use three-level loading:

1. **Level 1: Metadata** - Name + description (always loaded)
2. **Level 2: SKILL.md body** - Main instructions (loaded when skill triggers)
3. **Level 3: References** - Detailed docs (loaded on demand)

### Designing for Progressive Disclosure

```
SKILL.md (Level 2)
├── Quick overview
├── When to use
├── Common patterns (inline)
└── Pointers to references

references/ (Level 3)
├── Detailed API docs
├── Advanced examples
└── Edge cases
```

Users get fast answers from SKILL.md, deep dives from references.

---

## Writing Guidelines

### Be Concise
- Favor examples over explanations
- One concept per section
- Use bullet points, not paragraphs

### Be Specific
- Include exact function names
- Show real code, not pseudocode
- Mention version numbers if relevant

### Be Actionable
- Start sections with verbs: "Create", "Configure", "Handle"
- Provide copy-paste code
- Include expected outputs

### Structure for Scanning
```markdown
## Section Title

Brief context (1-2 sentences max).

**Quick reference:**
- `function1()` - does X
- `function2(param)` - does Y

**Example:**
\```typescript
// Common pattern
const result = function1();
\```
```

---

## Common Patterns

### Pattern 1: Quick Reference Table

```markdown
## API Quick Reference

| Method | Description | Example |
|--------|-------------|---------|
| `create()` | Creates new instance | `client.create({...})` |
| `get(id)` | Retrieves by ID | `client.get("abc123")` |
| `update(id, data)` | Updates existing | `client.update("abc123", {...})` |
| `delete(id)` | Removes instance | `client.delete("abc123")` |
```

### Pattern 2: Code Template with Placeholders

```markdown
## Session Template

\```typescript
import { Client } from "example";

const client = new Client({
  apiKey: process.env.EXAMPLE_API_KEY, // Required
  // options: { ... }                  // Optional config
});

async function main() {
  // Your code here
}

main();
\```
```

### Pattern 3: Conditional Instructions

```markdown
## Error Handling

**If you see `AuthenticationError`:**
1. Check API key is set: `echo $EXAMPLE_API_KEY`
2. Verify key is valid in dashboard
3. Regenerate if expired

**If you see `RateLimitError`:**
1. Add delay between requests
2. Implement exponential backoff
3. Consider upgrading plan
```

### Pattern 4: Trigger Definition

```markdown
## When to Use This Skill

Activate when user:
- Mentions "browserbase", "browser automation", or "headless browser"
- Asks about "captcha solving" or "bot detection"
- Wants to "scrape" with managed infrastructure
- Encounters Playwright/Puppeteer scaling issues
```

---

## Skill Quality Checklist

Before publishing:

- [ ] SKILL.md has valid YAML frontmatter
- [ ] Description is specific and action-oriented
- [ ] Body is under 500 lines
- [ ] Code examples are tested and work
- [ ] Triggers are clearly defined
- [ ] References are linked, not duplicated
- [ ] No verbose explanations where code suffices
