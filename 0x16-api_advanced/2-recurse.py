#!/usr/bin/python3
"""Module for a recursive function"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit"""
    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code >= 400:
        return None

    after = hot_list + [child.get("data").get("title")
                        for child in response.json()
                        .get("data")
                        .get("children")]

    info = response.json()
    if not info.get("data").get("after"):
        return after

    return recurse(subreddit, after, info.get("data").get("count"),
                   info.get("data").get("after"))
