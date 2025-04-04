import requests


URL = f"https://api.api-ninjas.com/v1/animals?name="
API_KEY = "kkImrQgeUXU0frtzE8M79A==bN5xULXLZCNPD07f"


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        "name": ...,
        "characteristics": {
            ...
        },
        "locations": [
            ...
        ],
        ...
    }
    """
    api_url = URL + animal_name
    response = requests.get(api_url, headers={"X-Api-Key": API_KEY})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None