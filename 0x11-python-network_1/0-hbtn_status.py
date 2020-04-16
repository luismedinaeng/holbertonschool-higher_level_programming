#!/usr/bin/python3
'''
Request content of a page
'''

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        content = response.read()
        strp = "Body response:\n\t- type: {}"
        strp = strp + "\n\t- content: {}\n\t- utf8 content: {}"
        print(strp.format(type(content), content, content.decode("utf-8")))
