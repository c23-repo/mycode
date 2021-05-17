#!/usr/bin/python3
import re

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def is_good_response(resp):
    """
   Returns True if the response seems to be HTML, False otherwise.
   """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def simple_get(url):
    """
   Attempts to get the content at `url` by making an HTTP GET request.
   If the content-type of response is some kind of HTML/XML, return the
   text content, otherwise return None.
   """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
       # log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def get_names():
    """
   Downloads the page where the list of mathematicians is found
   and returns a list of strings, one per mathematician
   """
    url = 'https://hobbylark.com/fandoms/The-Epic-List-of-250-Legendary-Swords'
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        swords_dict = {}
        for li in html.select('li'):
            if ": " in li.text:
                sword_list = re.split("\:(.*)", li.text)
                if "Swords" not in sword_list[0]:
                    swords_dict[sword_list[0]] = sword_list[1]

        return swords_dict

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))


def main():
    print(get_names())


if __name__ == "__main__":
    main()

