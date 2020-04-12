#!/bin/bash
# Sends a GET request to the URL inserted as argument, and displays the body of the response
STATUS="$(curl -X GET -sI "$1" | grep "HTTP" | cut -d" " -f2)"

if [ "$STATUS" -eq 200 ];
then
		curl -X GET "$1"
fi
