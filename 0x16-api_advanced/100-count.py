#!/usr/bin/python3
""" Function to query Reddit API and return sorted count of keywords. """
import requests


def count_words(subreddit, word_list, after="", count=0, counts=None):
    """ Recursively count and print keywords
    in hot articles of a subreddit. """
    if counts is None:
        counts = {}

    link = f"https://www.reddit.com/r/{subreddit}/hot.json"
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
                title = post['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title:
                        if word in counts:
                            counts[word] += 1
                        else:
                            counts[word] = 1

            if after is not None:
                return count_words(subreddit, word_list, after, count, counts)
            else:
                if len(counts) > 0:
                    for word, count in sorted(counts.items(),
                                              key=lambda x: (-x[1], x[0])):
                        print(f"{word}: {count}")
                else:
                    print(None)
    except Exception:
        print(None)
