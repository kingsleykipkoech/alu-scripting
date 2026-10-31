#!/usr/bin/python3
"""Module that queries the Reddit API and prints top ten hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit.

    If the subreddit is invalid, prints None.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/kingsley)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code == 200:
            posts = response.json().get("data", {}).get("children", [])
            for post in posts:
                print(post.get("data", {}).get("title"))
        else:
            print(None)
    except Exception:
        print(None)
