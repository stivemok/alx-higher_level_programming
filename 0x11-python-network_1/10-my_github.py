#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import sys
import requests

if __name__ == '__main__':
resp = requests.get('https://api.github.com/user',
                    auth=requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2]))
json = resp.json()
print('{}'.format(json.get('id')))
