#!/usr/bin/python3
"""Module that queries the Reddit API and returns the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a given subreddit.

    If the subreddit is invalid, returns 0.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/kingsley)"
    }

    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        return 0
    except Exception:
        return 0
