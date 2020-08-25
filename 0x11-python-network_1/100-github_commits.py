#!/usr/bin/python3
""" Python Script that list 10 commits (from the most recent to oldest
    of the repository “rails” by the user “rails”
"""

import requests
from sys import argv


if __name__ == "__main__":
    repo_name = argv[1]
    owner_name = argv[2]
    url = 'https://api.github.com/repos/{}/{}'.format(owner_name, repo_name)
    url += '/commits?per_page=10'
    resp = requests.get(url)
    json_commits = resp.json()
    for commit in json_commits:
        sha = commit.get('sha')
        name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, name))
