"""
fetch_animals.py

Fetch data from the animals api
"""
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")


def fetch_animals_data(search_input):
    """Fetch data from the animals API.
    Use the search input from user as name"""

    url = f"https://api.api-ninjas.com/v1/animals?name={search_input}"
    headers = {
        'X-Api-Key': API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}: {response.text}")
        return []
