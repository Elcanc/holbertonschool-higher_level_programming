#!/usr/bin/python3
"""
Takes GitHub username and personal access token,
uses the GitHub API to display your user id.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    try:
        json_data = response.json()
        print(json_data.get("id"))
    except ValueError:
        print(None)
