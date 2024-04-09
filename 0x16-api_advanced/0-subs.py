#!/usr/bin/python3
"""import requests"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subcribers of a subreddit"""
    response = requests.get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit),
        headers={'User-Agent': 'AlxUser-Agent'},
        allow_redirects=False)
    if response.status_code < 300:
        return response.json().get('data')['subscribers']
    return 0
