#!/bin/bash
# Sends a GET request to the URL inserted as argument, and displays the body of the response
curl -sL "$1" -X GET
