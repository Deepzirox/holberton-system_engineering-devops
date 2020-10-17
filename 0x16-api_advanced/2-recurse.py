#!/usr/bin/python3
"""
queries the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """  function that queries the Reddit API
    """
    agent = "Holberton"
    header = {"User-Agent": agent}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"

    if after:
        url += '?after={}'.format(after)

    req = requests.get(url, headers=header).json()

    if req.get('error') == 404:
        return

    respon = req.get("data").get("children")

    for i in respon:
        hot_list.append(i.get('data').get('title'))

    after = req.get('data').get('after')

    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
