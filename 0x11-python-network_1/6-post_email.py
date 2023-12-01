#!/usr/bin/python3
"""This script sends a POST request to the passed URL with the email as a parameter
and finally displays the body of the response"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
