#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests
import sys

def top_ten(subreddit):
    # Construct the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}  # Specify User-Agent header

    # Make the GET request to Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        # Check if there are any posts
        if not posts:
            print("No posts found.")
        else:
            # Print the titles of the first 10 posts
            for post in posts:
                print(post['data']['title'])
    else:
        # Print None for invalid subreddits or other errors
        print("None")

# Example usage when the script is run directly
if __name__ == "__main__":
    import sys

    # Check if a subreddit argument is provided
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        # Call the top_ten function with the provided subreddit
        top_ten(sys.argv[1])
