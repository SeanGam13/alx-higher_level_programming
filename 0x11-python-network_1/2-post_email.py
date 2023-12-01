#!/usr/bin/python3
"""This script takes in a URL and an email, sends a POST request to the request to the
passed URL with the email as a parameter, and displays the body of the response"""
import sys
from urllib.request import urlopen
from urllib.parse import urlencode

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urlencode({'email': email}).encode('utf-8')
    with urlopen(url, data) as response:
        body = response.read()
        print(body.decode('utf-8'))
