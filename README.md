# Claude Skills

A collection of skills for [Claude Code](https://claude.ai/claude-code) for content creation, developer tooling, and more.

## What are Skills?

Skills are markdown files that give AI agents specialized knowledge and workflows for specific tasks. When added to your project, Claude Code recognizes relevant contexts and applies the right frameworks automatically.

## Available Skills

| Skill | Description |
|-------|-------------|
| [writing-linkedin-posts](./skills/writing-linkedin-posts/) | Create engaging, authentic LinkedIn posts by learning your voice from existing posts |
| [docs-to-skill](./skills/docs-to-skill/) | Convert online documentation into Claude Code skills with working scripts and proper structure |

## Installation

### Option 1: CLI Install (Recommended)

```bash
npx skills add jaysahnan/skills
```

Or install a specific skill:

```bash
npx skills add jaysahnan/skills/writing-linkedin-posts
```

### Option 2: Clone and Copy

```bash
git clone https://github.com/jaysahnan/skills.git
cp -r skills/skills/* ~/.claude/skills/
```

### Option 3: Git Submodule

```bash
git submodule add https://github.com/jaysahnan/skills.git .claude/skills/jaysahnan
```

## Usage

Once installed, invoke skills through natural requests:

- "Write a LinkedIn post about [topic]"
- "Help me create a thought leadership post"
- "Convert the Stripe docs into a skill"

Or use direct commands:

```
/writing-linkedin-posts
/docs-to-skill https://docs.example.com
```

## Adding New Skills

Each skill lives in its own folder under `skills/`:

```
skills/
├── writing-linkedin-posts/
│   ├── SKILL.md          # Main skill definition
│   ├── README.md         # Skill documentation
│   ├── scripts/          # Supporting scripts
│   └── references/       # Reference materials
└── your-new-skill/
    └── SKILL.md
```

## Contributing

Contributions welcome! Feel free to open issues or submit PRs.

## License

MIT
