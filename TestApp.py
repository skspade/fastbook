import os
import requests


def search_images_in_bing(key, term, min_sz=128, max_images=150):
    url = "https://bing-image-search1.p.rapidapi.com/images/trending"
    headers = {
        "X-RapidAPI-Key": "374ba3c7b1msh7444a134ac05df6p1cce40jsn7fd5b767d681",
        "X-RapidAPI-Host": "bing-image-search1.p.rapidapi.com"
    }
    return requests.request("GET", url, headers=headers)


results = search_images_in_bing(key, 'grizzly bear')
images = results.json()['value']
len(images)
