#!/usr/bin/python3
""" Queries Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers for a given subreddit """ 
    headers = {"User-Agent": "CustomUser"}
    link = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(link, headers=headers)
        return (response.json()['data']['subscribers'])
    except KeyError:
        return 0
