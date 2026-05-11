import sys
import io

if hasattr(sys.stdin, 'buffer'):
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

from scraper import search_places
from exporter import export_to_excel

def deduplicate(places):
    seen = set()
    unique = []
    for place in places:
        name = place.get("displayName", {}).get("text", "")
        address = place.get("formattedAddress", "")
        key = (name, address)
        if key not in seen:
            seen.add(key)
            unique.append(place)
    return unique

def main():
    city = input("City: ").strip()
    query = input("Search keyword: ").strip()

    if not city or not query:
        print("City and keyword cannot be empty.")
        return

    print(f"\nSearching for '{query}' in {city}...")
    places = search_places(city, query)

    if not places:
        print("No results found.")
        return

    places = deduplicate(places)
    print(f"Found {len(places)} unique results.")

    filepath = export_to_excel(places, city, query)
    print(f"Saved to: {filepath}")

if __name__ == "__main__":
    main()
