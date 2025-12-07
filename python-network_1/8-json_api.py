#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with the letter provided as q and displays the result.
"""
import requests
import sys

if __name__ == "__main__":
    # Arqument yoxlanması, əgər verilən yoxdursa q=""
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {"q": q}

    try:
        response = requests.post("http://0.0.0.0:5000/search_user", data=data)
        json_data = response.json()  # JSON çevirməyə çalışır

        if json_data:
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
