import os
import requests


def search_images_in_bing(key, term, min_sz=128, max_images=150):
    url = "https://bing-image-search1.p.rapidapi.com/images/search"

    querystring = {"q": term, "count":"150", "min_height": min_sz, "min_width": min_sz}

    headers = {
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": "bing-image-search1.p.rapidapi.com"
    }
    return requests.request("GET", url, headers=headers, params=querystring)


key = "374ba3c7b1msh7444a134ac05df6p1cce40jsn7fd5b767d681"
results = search_images_in_bing(key, 'grizzly bear')
imagesResult = results.json()
images = imagesResult['value']
print(images)
len(images)

# %%

# %%

# %%

# %%

# %%
