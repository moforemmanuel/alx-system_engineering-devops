#!/usr/bin/python3
"""return the number of subscribers of a reddit sub"""

import requests
import sys


def number_of_subscribers(subreddit):
    """function"""
    data = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False)

    if data.status_code >= 300:
        return 0
    return data.json().get("data").get("subscribers")


if __name__ == '__main__':
    print(number_of_subscribers('football'))
