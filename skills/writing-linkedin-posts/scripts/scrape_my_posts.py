#!/usr/bin/env python3
"""
Scrape LinkedIn posts from a profile using Apify's linkedin-profile-posts actor.
Caches results locally to avoid re-fetching during iterative drafting.

Usage:
    python scrape_my_posts.py [--limit 50] [--refresh]

Environment variables (set in ~/.zshrc):
    LINKEDIN_USERNAME - Your LinkedIn username
    APIFY_TOKEN - Your Apify API token
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

CACHE_DIR = Path(__file__).parent.parent / "cache"


def print_setup_instructions(missing_username: bool, missing_token: bool):
    """Print setup instructions for missing env vars."""
    print("\n" + "=" * 50, file=sys.stderr)
    print("SETUP REQUIRED", file=sys.stderr)
    print("=" * 50, file=sys.stderr)

    if missing_token:
        print("\n1. Get an Apify API token:", file=sys.stderr)
        print("   https://console.apify.com/settings/integrations", file=sys.stderr)

    if missing_username:
        print("\n2. Find your LinkedIn username:", file=sys.stderr)
        print("   It's the last part of your profile URL", file=sys.stderr)
        print("   e.g., linkedin.com/in/jaysahnan -> jaysahnan", file=sys.stderr)

    print("\n3. Add to your ~/.zshrc:", file=sys.stderr)
    print("   " + "-" * 40, file=sys.stderr)
    if missing_token:
        print('   export APIFY_TOKEN="your_token_here"', file=sys.stderr)
    if missing_username:
        print('   export LINKEDIN_USERNAME="your_username"', file=sys.stderr)
    print("   " + "-" * 40, file=sys.stderr)

    print("\n4. Then run: source ~/.zshrc", file=sys.stderr)
    print("=" * 50 + "\n", file=sys.stderr)


def get_cache_path(username: str) -> Path:
    """Get the cache file path for a username."""
    clean_username = username.lower().replace("/", "_").replace("\\", "_")
    return CACHE_DIR / f"{clean_username}_posts.json"


def load_cached_posts(username: str) -> dict | None:
    """Load cached posts if they exist."""
    cache_path = get_cache_path(username)
    if cache_path.exists():
        try:
            with open(cache_path, "r") as f:
                cached = json.load(f)
                cached_at = cached.get("cached_at", "Unknown")
                post_count = len(cached.get("posts", []))
                print(f"Using cached posts ({post_count} posts from {cached_at})", file=sys.stderr)
                print(f"Use --refresh to fetch new posts\n", file=sys.stderr)
                return cached
        except (json.JSONDecodeError, IOError):
            return None
    return None


def save_posts_to_cache(username: str, posts: list) -> None:
    """Save posts to cache file."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = get_cache_path(username)

    cache_data = {
        "username": username,
        "cached_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "post_count": len(posts),
        "posts": posts
    }

    with open(cache_path, "w") as f:
        json.dump(cache_data, f, indent=2)

    print(f"Cached {len(posts)} posts to {cache_path}", file=sys.stderr)


def scrape_linkedin_posts(username: str, token: str, limit: int = 50) -> list:
    """
    Scrape posts from a LinkedIn profile using Apify.

    Args:
        username: LinkedIn username (e.g., 'satyanadella' or full URL)
        token: Apify API token
        limit: Number of posts to retrieve (default 50)

    Returns:
        list of posts
    """
    # Clean username if full URL provided
    if "linkedin.com" in username:
        username = username.rstrip("/").split("/")[-1]

    # Apify actor endpoint (run synchronously and get dataset items)
    url = f"https://api.apify.com/v2/acts/apimaestro~linkedin-profile-posts/run-sync-get-dataset-items?token={token}"

    # Input payload
    payload = {
        "username": username,
        "page_number": 1,
        "limit": min(limit, 100)  # API max is 100
    }

    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=300) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result if isinstance(result, list) else []
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else ""
        print(f"Error: HTTP {e.code}: {e.reason}", file=sys.stderr)
        if error_body:
            print(f"Details: {error_body}", file=sys.stderr)
        return []
    except urllib.error.URLError as e:
        print(f"Error: Connection error: {e.reason}", file=sys.stderr)
        return []
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return []


def format_posts_for_analysis(posts: list, original_only: bool = True) -> str:
    """Format scraped posts for tone analysis."""
    output = []
    post_num = 0

    for post in posts:
        if not isinstance(post, dict):
            continue

        # Skip reposts if original_only is True
        post_type = post.get("post_type", "")
        if original_only and post_type == "repost":
            continue

        text = post.get("text", "").strip()
        if not text:
            continue

        post_num += 1
        stats = post.get("stats", {})
        reactions = stats.get("total_reactions", 0)
        comments = stats.get("comments", 0)
        reposts = stats.get("reposts", 0)
        posted_at = post.get("posted_at", {})
        date_str = posted_at.get("date", "Unknown") if isinstance(posted_at, dict) else str(posted_at)
        media = post.get("media", {})
        media_type = media.get("type", "none") if isinstance(media, dict) else "none"

        output.append(f"--- POST {post_num} ---")
        output.append(f"Date: {date_str}")
        output.append(f"Engagement: {reactions} reactions, {comments} comments, {reposts} reposts")
        output.append(f"Media: {media_type}")
        output.append(f"\n{text}\n")

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(
        description="Scrape LinkedIn posts for tone/style analysis (with caching)"
    )
    parser.add_argument("--username", "-u",
                        default=os.environ.get("LINKEDIN_USERNAME", ""),
                        help="LinkedIn username (default: LINKEDIN_USERNAME env var)")
    parser.add_argument("--token", "-t",
                        default=os.environ.get("APIFY_TOKEN", ""),
                        help="Apify API token (default: APIFY_TOKEN env var)")
    parser.add_argument("--limit", type=int, default=50,
                        help="Number of posts to fetch (default: 50)")
    parser.add_argument("--refresh", action="store_true",
                        help="Force refresh from API (ignore cache)")
    parser.add_argument("--raw", action="store_true",
                        help="Output raw JSON instead of formatted text")
    parser.add_argument("--include-reposts", action="store_true",
                        help="Include reposts (default: original posts only)")

    args = parser.parse_args()

    # Check for missing config
    missing_username = not args.username
    missing_token = not args.token

    # Clean username if provided
    username = args.username
    if username and "linkedin.com" in username:
        username = username.rstrip("/").split("/")[-1]

    # Try to load from cache first (unless --refresh)
    posts = None
    if username and not args.refresh:
        cached = load_cached_posts(username)
        if cached:
            posts = cached.get("posts", [])

    # If we have cached posts, we don't need the token
    if posts:
        pass  # Good to go
    elif missing_username or missing_token:
        # Need to fetch but missing config
        print_setup_instructions(missing_username, missing_token)
        if missing_username:
            print("Or provide username now: --username YOUR_USERNAME", file=sys.stderr)
        if missing_token:
            print("Or provide token now: --token YOUR_TOKEN", file=sys.stderr)
        sys.exit(1)
    else:
        # Fetch from API
        print(f"Fetching posts from LinkedIn: {username}", file=sys.stderr)
        print(f"Limit: {args.limit} posts", file=sys.stderr)
        print("This may take a minute...\n", file=sys.stderr)

        posts = scrape_linkedin_posts(username, args.token, args.limit)

        if posts:
            save_posts_to_cache(username, posts)
        else:
            print("No posts retrieved.", file=sys.stderr)
            sys.exit(1)

    # Output results
    if args.raw:
        print(json.dumps(posts, indent=2))
    else:
        original_only = not args.include_reposts
        formatted = format_posts_for_analysis(posts, original_only=original_only)
        if formatted:
            print(formatted)
        else:
            if original_only:
                print("No original posts found. Try --include-reposts to see all activity.", file=sys.stderr)
            else:
                print("No posts found.", file=sys.stderr)


if __name__ == "__main__":
    main()
