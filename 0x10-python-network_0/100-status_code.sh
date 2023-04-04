#!/bin/bash
# Sends a GET request to a given URL and display the response status code.
curl -s "$1" -o /dev/null -w "%{http_code}"
