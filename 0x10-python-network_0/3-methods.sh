#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept
curl -sI "$2" | grep "Allow:" | cut -d ' ' -f2-
