#!/bin/bash
# Sends a GET request to a given URL and display the response status code.
curl -sI "$1" | grep -i HTTP | awk '{print $2}'
