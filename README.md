# Claude Skills

A collection of skills for [Claude Code](https://claude.ai/claude-code).

## Installation

Install skills using the skills CLI:

```bash
npx skills add jaysahnan/claude-skills
```

Or install a specific skill:

```bash
npx skills add jaysahnan/claude-skills/writing-linkedin-posts
```

## Available Skills

| Skill | Description |
|-------|-------------|
| [writing-linkedin-posts](./skills/writing-linkedin-posts/) | Create engaging, authentic LinkedIn posts by learning your voice |

## Manual Installation

Clone this repo and add to your Claude settings:

```bash
git clone https://github.com/jaysahnan/claude-skills.git ~/.claude/skills/jaysahnan
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

## License

MIT
