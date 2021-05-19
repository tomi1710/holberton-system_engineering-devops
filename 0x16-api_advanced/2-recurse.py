#!/usr/bin/python3
""" Write a recursive function that queries the Reddit API and
    returns a list containing the titles of all hot articles for
    a given subreddit. If no results are found for the given
    subreddit, the function should return None """
import requests


def recurse(subreddit, hot_list=[], next_page=''):
    """ def """
    page = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, next_page)
    req = requests.get(page, headers={"User-Agent": "Mozilla/5.0"},
                       allow_redirects=False)
    json_req = req.json()
    if req.status_code != 200:
        return None
    else:
        posts = json_req.get('data').get('children')
        for title in posts:
            hot_list.append(title.get('data').get('title'))
        next_page = json_req.get('data').get('after')
        if next_page is not None:
            recurse(subreddit, hot_list, next_page)
        return hot_list
