# Writing LinkedIn Posts

Create engaging, authentic LinkedIn posts that sound like you—not generic LinkedIn content.

## What It Does

This skill scrapes your existing LinkedIn posts to learn your authentic voice, then writes new posts that match your style. It uses research-backed data on hooks and LinkedIn algorithm patterns.

## Setup

The skill requires two environment variables:

1. **Get an Apify API token** (free tier available):
   https://console.apify.com/settings/integrations

2. **Find your LinkedIn username** (last part of your profile URL):
   `linkedin.com/in/yourname` → `yourname`

3. **Add to your shell config** (`~/.zshrc` or `~/.bashrc`):
   ```bash
   export APIFY_TOKEN="your_token_here"
   export LINKEDIN_USERNAME="your_username"
   ```

4. **Reload your shell**:
   ```bash
   source ~/.zshrc
   ```

## Usage

Ask Claude to write a LinkedIn post:

- "Write a LinkedIn post about [topic]"
- "Help me with a LinkedIn post"
- "Create a thought leadership post about [topic]"

The skill will:
1. Scrape your recent posts (cached locally)
2. Analyze your voice patterns
3. Write a post matching your style
4. Offer to copy to clipboard

## Files

- `SKILL.md` - Main skill definition with writing guidelines
- `scripts/scrape_my_posts.py` - LinkedIn scraper with caching
- `references/hooks.md` - Research-backed hook patterns
- `references/examples.md` - LinkedIn algorithm data (2025)

## License

MIT
