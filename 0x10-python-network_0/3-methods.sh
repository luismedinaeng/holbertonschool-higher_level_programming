#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -X OPTIONS -sI "$1" | sed -n -e 's/^Allow: //p'
