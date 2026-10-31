#!/usr/bin/python3
"""Module that queries the Reddit API and prints top ten hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit.

    If the subreddit is invalid, prints None.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json().get("data", {})
            children = data.get("children", [])
            if not children:
                print(None)
                return
            for child in children[:10]:
                print(child.get("data", {}).get("title"))
        else:
            print(None)
    except Exception:
        print(None)
