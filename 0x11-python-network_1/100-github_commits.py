#!/usr/bin/python3
'''
Lists teh last 10 commits on a repository
'''
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"
    response = requests.get(url.format(sys.argv[2], sys.argv[1]))
    a = 0
    for i in response.json():
        print("{}: {}".format(i['sha'], i['commit']['author']['name']))
        a = a + 1
        if a == 10:
            break
