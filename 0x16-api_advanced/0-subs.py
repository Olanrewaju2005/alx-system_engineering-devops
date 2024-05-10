#!/usr/bin/bash
"""
import important modules
"""
import requests

def number_of_subscribers(subreddit):
    """
    function queries reddit api and returns the number
    of subcribers
    """
    url = f"https://www.reddit.com/dev/api/"
    headers = {'User-Agent': ''}

    try:
        response = 
