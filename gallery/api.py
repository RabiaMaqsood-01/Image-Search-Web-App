

import requests
import random

def fetch_pexels_photos(query=None, page=1):
    headers = {
        'Authorization': 'FSJwyIOwU8jM3uUp1bJkUam8TfqbGa2G0tY1IENarDFqds6pcFDXMF2X'
    }

    if not query:
        # Use a random page for curated photos (e.g., 1 to 50)
        page = random.randint(1, 50)
        url = f'https://api.pexels.com/v1/curated?per_page=15&page={page}'
    else:
        url = f'https://api.pexels.com/v1/search?query={query}&per_page=15&page={page}'

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get('photos', [])
    except requests.RequestException as e:
        print(f"Error fetching Pexels photos: {e}")
        return []
