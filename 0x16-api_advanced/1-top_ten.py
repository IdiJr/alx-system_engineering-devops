#!/usr/bin/python3
""" Queries the Reddit API and prints the titles of the first 10 hot posts """
import requests


def top_ten(subreddit):
    """ Print the titles of the first 10 hot posts for a given subreddit. """
    headers = {"User-Agent": "CustomUser"}
    link = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(link, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    posts = response.json()['data']['children']
    for post in range(0, 10):
        print(posts[post]['data']['title'])
