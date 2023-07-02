#!/usr/bin/python3
""" takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ''
    resp = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        response = resp.json()
        if response:
            print('[{}] {}'.format(response.get('id', response.get('name')))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
