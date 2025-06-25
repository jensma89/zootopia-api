"""
fetch_animals.py

get the data from the animals api
"""
import requests

def get_animals_data():
    url = "https://api.api-ninjas.com/v1/animals?name=seal"
    headers = {
        'X-Api-Key': 'eMuvHY30wqN+Soz7l0HJHA==PJ1x1be6vxNPtgNq'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for animal in data:
            print(f"{animal['name']} - {animal['characteristics']['diet']}")
    else:
        print(f"Error: {response.status_code}: {response.text}")


if __name__ == "__main__":
    get_animals_data()