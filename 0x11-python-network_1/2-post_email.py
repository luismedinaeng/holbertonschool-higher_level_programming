#!/usr/bin/python3
'''
takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays
the body of the response
'''
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
