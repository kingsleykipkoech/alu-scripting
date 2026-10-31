# API Advanced: Reddit API & Recursion

This project covers consuming remote APIs with pagination, setting custom User-Agents to prevent rate limiting, parsing nested JSON datasets, and implementing clean recursive functions without iterative loops.

## Learning Objectives
* Reading external API documentation
* Using query strings and pagination tokens (`after`)
* Parsing JSON structures with safe dictionary `.get()`
* Writing recursive API calls in Python
* Sorting dictionaries by value descending and key ascending

## Tasks Overview

### [0. How many subs?](./0-subs.py)
Queries the Reddit API (`/r/{subreddit}/about.json`) and returns the total subscriber count for a given subreddit. If the subreddit is invalid, returns 0 without following redirects.

### [1. Top Ten](./1-top_ten.py)
Queries the Reddit API (`/r/{subreddit}/hot.json`) and prints the titles of the first 10 hot posts. If invalid, prints `None`.

### [2. Recurse it!](./2-recurse.py)
Recursive function that queries the Reddit API and returns a list containing titles of all hot articles for a given subreddit by handling pagination recursively without any loops.

### [3. Count it!](./3-count.py)
Recursive function that parses titles of all hot articles, counts occurrences of specified keywords (case-insensitive, exact matches), and prints sorted counts descending (and alphabetically ascending for ties).

## Requirements
* All files interpreted using Python 3.4+
* PEP 8 compliant (`pycodestyle`)
* Modules and functions are documented
* All files are executable (`chmod +x`)
