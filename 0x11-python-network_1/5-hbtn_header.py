#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL and displays the value
    of the variable X-Request-Id in the response header
"""
import requests
import sys


req = requests.get(sys.argv[1]).headers
print(req.get("X-Request-Id"))
