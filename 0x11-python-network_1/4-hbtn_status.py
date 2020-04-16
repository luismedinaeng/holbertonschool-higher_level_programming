#!/usr/bin/python3
'''
fetches https://intranet.hbtn.io/status
'''
import requests

if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    strp = "Body response:\n\t- type: {}\n\t- content: {}"
    print(strp.format(type(response.text), response.text))
