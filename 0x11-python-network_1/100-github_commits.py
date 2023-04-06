#!/usr/bin/python3
""" Lists the recent 10 commits in a Github repository and the committer
"""
import sys
import requests

if __name__ == "__main__":
    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    r = requests.get(url)

    commit_history = r.json()
    for commit in commit_history[:10]:
        sha = commit.get("sha")
        committer = commit["commit"]["author"]["name"]
        print(f"{sha}: {committer}")
