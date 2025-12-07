#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter.
Displays the body of the response decoded in UTF-8.
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # POST data hazırlamaq
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    # POST request göndərmək
    req = urllib.request.Request(url, data=data)

    # Response almaq
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode("utf-8"))
