import requests
from config import API_KEY

URL = "https://places.googleapis.com/v1/places:searchText"

HEADERS = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": API_KEY,
    "X-Goog-FieldMask": (
        "places.displayName,places.formattedAddress,"
        "places.nationalPhoneNumber,places.rating,places.websiteUri"
    )
}

def search_places(city, query):
    all_places = []
    page_token = None

    while True:
        body = {
            "textQuery": f"{query} {city}",
            "languageCode": "uk"
        }
        if page_token:
            body["pageToken"] = page_token

        try:
            response = requests.post(URL, headers=HEADERS, json=body, timeout=15)
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            break

        if not response.ok:
            print(f"API error {response.status_code}: {response.text}")
            break

        data = response.json()

        if "error" in data:
            msg = data["error"].get("message", "Unknown error")
            print(f"API error: {msg}")
            break

        places = data.get("places", [])
        all_places.extend(places)

        page_token = data.get("nextPageToken")
        if not page_token:
            break

    return all_places
