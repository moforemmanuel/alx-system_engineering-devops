#!/usr/bin/python3
"""number of subscribers of a reddit sub"""


def number_of_subscribers(subreddit):
    """query function"""
    import requests

    data = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False)

    if data.status_code >= 300:
        return 0
    return data.json().get("data").get("subscribers")
