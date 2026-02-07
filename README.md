# Claude Skills

A collection of skills for [Claude Code](https://claude.ai/claude-code) focused on content creation and social media.

## What are Skills?

Skills are markdown files that give AI agents specialized knowledge and workflows for specific tasks. When added to your project, Claude Code recognizes relevant contexts and applies the right frameworks automatically.

## Available Skills

| Skill | Description |
|-------|-------------|
| [writing-linkedin-posts](./skills/writing-linkedin-posts/) | Create engaging, authentic LinkedIn posts by learning your voice from existing posts |

## Installation

### Option 1: CLI Install (Recommended)

```bash
npx skills add jaysahnan/claude-skills
```

Or install a specific skill:

```bash
npx skills add jaysahnan/claude-skills/writing-linkedin-posts
```

### Option 2: Clone and Copy

```bash
git clone https://github.com/jaysahnan/claude-skills.git
cp -r claude-skills/skills/* ~/.claude/skills/
```

### Option 3: Git Submodule

```bash
git submodule add https://github.com/jaysahnan/claude-skills.git .claude/skills/jaysahnan
```

## Usage

Once installed, invoke skills through natural requests:

- "Write a LinkedIn post about [topic]"
- "Help me create a thought leadership post"
- "Draft a LinkedIn post in my voice"

Or use direct commands:

```
/writing-linkedin-posts
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
