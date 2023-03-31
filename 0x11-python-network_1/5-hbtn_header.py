#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL and displays the value
    of the variable X-Request-Id in the response header
"""
import requests


url = 'https://alx-intranet.hbtn.io/status'
req = requests.get(url).headers
print(req.get("X-Request-Id"))
