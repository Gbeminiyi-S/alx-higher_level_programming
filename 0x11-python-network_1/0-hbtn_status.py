#!/usr/bin/python3
"""Fetches a url using urllib
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        html = response.read()
    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
    print(f"\t- utf8 content: {html.decode('utf-8')}")"""

'''a python script that fetches a url using urllib'''
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
    print('Body response:')
    print('\t- type: {}'.format(type(content)))
    print(f'\t- content: {content}')
    print(f'\t- utf8 content: {content.decode("utf-8")}')
