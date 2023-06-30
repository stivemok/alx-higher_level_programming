#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and
displays the body of the response(decoded in utf-8)"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    parameter = {'email': sys.argv[2]}
    email = urllib.parse.urlencode(parameter)
    data = email.encode()
    url = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(url) as response:
        resp = response.read()
        print(resp.decode('utf-8'))
