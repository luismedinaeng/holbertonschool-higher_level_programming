#!/bin/bash
# Displays the size of the body of the response returned by a request to a URL
curl -sI "$1" | sed -n -e 's/^Content-Length: //p'
