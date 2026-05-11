import os
from datetime import date
from openpyxl import Workbook
from openpyxl.styles import Font

COLUMNS = ["Company Name", "Phone", "Website", "Address", "Rating", "Search Query", "City", "Date Scraped"]

_BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def export_to_excel(places, city, query, output_dir=None):
    if output_dir is None:
        output_dir = os.path.join(_BASE_DIR, "results")
    os.makedirs(output_dir, exist_ok=True)

    today = date.today().strftime("%Y-%m-%d")
    safe_city = city.replace(" ", "_")
    safe_query = query.replace(" ", "_")
    filepath = os.path.join(output_dir, f"{safe_city}_{safe_query}_{today}.xlsx")

    wb = Workbook()
    ws = wb.active
    ws.title = "Results"

    ws.append(COLUMNS)
    for cell in ws[1]:
        cell.font = Font(bold=True)

    for place in places:
        ws.append([
            place.get("displayName", {}).get("text", ""),
            place.get("nationalPhoneNumber", ""),
            place.get("websiteUri", ""),
            place.get("formattedAddress", ""),
            place.get("rating", ""),
            query,
            city,
            today,
        ])

    wb.save(filepath)
    return filepath
