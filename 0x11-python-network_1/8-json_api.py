#!/usr/bin/python3
'''
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
import sys
import requests

if __name__ == "__main__":
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    response = requests.post("http://0.0.0.0:5000/search_user",
                             data={'q': q})
    try:
        info = response.json()
    except:
        print("Not a valid JSON")
    else:
        if len(info) == 0:
            print("No result")
        else:
            print("[{}] {}".format(info['id'], info['name']))
