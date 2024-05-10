#!/usr/bin/python3
"""
Function to count words in all hot posts of a given subreddit
"""
import requests
import sys

def count_words(subreddit, word_list, after=None, counts={}):
    """
    recursive function that Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords
    """
    if not word_list or word_list == [] or not subreddit:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'Mozilla/10.0/API'}

    params = {'limit': 100}

    if after:
        params['after'] = after

    response = requests.get(url,
                            headers=headers,
                            params=params,  allow_redirects=False)

    if response.status_code != 200:
        return
    main_data = response.json()

    data = main_data.get('data')

    children = data.get('children')

    for post in children:
        title = post.get('data', {}).get('title').lower()

        for word in word_list:
            if word.lower() in title:
                counts[word] =  counts.get(word, 0) + title.count(word.lower())

    after = main_data.get('data', {}).get('after')

    if  after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0].lower()))

        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
