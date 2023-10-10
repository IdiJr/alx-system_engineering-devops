#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """ Recursively retrieve the top 10 hot articles for a given subreddit. """
    link = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "CustomUser"}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    try:
        response = requests.get(link, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            after = data['data']['after']
            for post in posts:
                hot_list.append(post['data']['title'])
            if after is not None:
                return recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    except Exception:
        return None
    if response.status_code == 404:
        return None
