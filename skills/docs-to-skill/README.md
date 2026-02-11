# docs-to-skill

Convert any online documentation into a Claude Code skill—complete with working scripts, reference files, and proper structure.

## Why This Skill?

Creating Claude Code skills from documentation is tedious: you have to crawl pages, extract code patterns, write examples, and structure everything properly. This skill automates the entire process.

Give it a docs URL, and it will:
- Crawl the documentation intelligently (using llms.txt/sitemap when available)
- Extract code patterns, API signatures, and environment variables
- Generate working, runnable scripts
- Create a properly structured skill with SKILL.md + references

## Installation

```bash
npx skills add jay-sahnan/skills/skills/docs-to-skill
```

## Usage

Invoke the skill with a documentation URL:

```
/docs-to-skill https://docs.stripe.com
```

Or naturally:

- "Convert the Browserbase docs into a skill"
- "Create a Claude skill from https://docs.anthropic.com"
- "Turn the Playwright documentation into a skill I can use"

## What Gets Generated

```
skills/<name>/
├── SKILL.md              # Main skill instructions
├── scripts/
│   ├── quickstart.ts     # Minimal working example
│   └── examples/         # Feature-specific scripts
├── references/
│   ├── api-reference.md  # Detailed API docs
│   └── examples.md       # Code patterns
├── package.json          # Dependencies
└── .env.example          # Required env vars
```

## Tips

- **Smaller docs = better results** — Skills from focused documentation (30-50 pages) turn out better than massive API references
- **Review before using** — The skill generates a good starting point; you may want to refine the SKILL.md

## No Setup Required

This skill uses WebFetch to crawl documentation—no API keys or configuration needed.

## License

MIT
