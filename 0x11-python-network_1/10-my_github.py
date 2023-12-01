#!/usr/bin/python3
"""This script takes your GitHub credentials (username and password) and uses the GitHub API to display your id"""
import requests
import sys

if __name__ == "__main__":
username = sys.argv[1]
password = sys.argv[2]
url = 'https://api.github.com/user'
headers = {
'Accept': 'application/vnd.github.v3+json',
'Username': username,
'Authorization': 'token {}'.format(password),
}
r = requests.get(url, headers=headers)
if r.ok:
json_data = r.json()
print(json_data.get('id', None))
else:
print(None)
