#!/usr/bin/python3
"""import requests"""
import requests


def top_ten(subreddit):
    """print the title of the hots post for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    response = requests.get(url,
                            headers={'User-Agent': 'ALX-Agent'},
                            allow_redirects=False)
    if response.status_code < 300:
        data = response.json().get('data').get('children')
        for i in range(0, 10):
            print(data[i].get('data').get('title'))
    else:
        print(None)
