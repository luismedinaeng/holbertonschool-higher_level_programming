#!/bin/bash
# Sends a GET request to the URL inserted as argument, and displays the body of the response
STATUS="$(curl -X GET -sIL "$1" | grep "^HTTP/1\.. 200" -c)"

if [ "$STATUS" -eq 1 ];
then
    curl -X GET "$1" -L
fi
