# Writing LinkedIn Posts

Create engaging, authentic LinkedIn posts that sound like *you*—not generic LinkedIn content.

## Why This Skill?

Most AI-written LinkedIn posts sound the same. This skill is different: it scrapes your existing posts to learn your authentic voice, then writes new content that matches your style, tone, and formatting patterns.

It also includes research-backed data on hooks and LinkedIn algorithm patterns from 2025.

## Installation

Add this skill to Claude Code:

```bash
claude install-skill https://github.com/jay-sahnan/skills/tree/main/skills/writing-linkedin-posts
```

## Setup (2 minutes)

This skill needs two environment variables to scrape your LinkedIn posts.

### Step 1: Get an Apify API Token (free)

1. Go to [console.apify.com](https://console.apify.com) and create a free account
2. Navigate to **Settings** → **Integrations**
3. Click **+ Add token** and name it (e.g., "linkedin-scraper")
4. Copy the token (it starts with `apify_api_`)

### Step 2: Find Your LinkedIn Username

Your username is the last part of your LinkedIn profile URL:

```
linkedin.com/in/jaysahnan
                 ^^^^^^^^
                 This is your username
```

### Step 3: Add Environment Variables

Add these to your shell config (`~/.zshrc` on Mac, `~/.bashrc` on Linux):

```bash
export APIFY_TOKEN="apify_api_your_token_here"
export LINKEDIN_USERNAME="your_username"
```

Then reload your shell:

```bash
source ~/.zshrc
```

### Verify Setup

Run this to confirm your variables are set:

```bash
echo $APIFY_TOKEN $LINKEDIN_USERNAME
```

## Usage

Just ask Claude to write a LinkedIn post:

- "Write a LinkedIn post about launching my new product"
- "Help me write a post about a lesson I learned this week"
- "Create a thought leadership post about remote work"
- "I want to share my thoughts on [topic] on LinkedIn"

### What Happens

1. **First run**: Claude scrapes your recent LinkedIn posts (takes ~30 seconds)
2. **Analysis**: Your posts are analyzed for voice, tone, hooks, and formatting patterns
3. **Writing**: New posts are written matching your authentic style
4. **Caching**: Your posts are cached locally so future runs are instant

### Tips

- The more posts you have on LinkedIn, the better it can learn your voice
- Use `--refresh` flag in the scraper to fetch your latest posts
- Posts are cached in `cache/` (gitignored, stays on your machine)

## Privacy

- Your credentials stay in your local environment variables
- Scraped posts are cached locally on your machine only
- Nothing is sent anywhere except the Apify API (to fetch your public posts)

## License

MIT
