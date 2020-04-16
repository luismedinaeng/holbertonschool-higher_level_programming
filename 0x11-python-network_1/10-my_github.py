#!/usr/bin/python3
'''
takes your Github credentials (username and password) and
uses the Github API to display your id
'''
import sys
import requests

if __name__ == "__main__":
    response = requests.get("https://api.github.com/user",
                            auth=(sys.argv[1], sys.argv[2]))
    if response.status_code == 200:
        print(response.json()['id'])
    else:
        print('None')
