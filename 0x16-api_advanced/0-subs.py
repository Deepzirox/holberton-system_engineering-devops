#!/usr/bin/python3
"""
queries the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """ Use the reddit API
    """
    agent = "Holberton"
    header = {"User-Agent": agent}
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"

    req = requests.get(url, headers=header)

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
