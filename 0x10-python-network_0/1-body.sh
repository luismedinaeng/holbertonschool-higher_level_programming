#!/bin/bash
# Sends a GET request to the URL inserted as argument, and displays the body of the response
STATUS="$(curl -w "%{http_code}" -sL "$1" -o /dev/null)"

if [ "$STATUS" -eq 1 ];
then
    curl -X GET "$1" -L
fi
