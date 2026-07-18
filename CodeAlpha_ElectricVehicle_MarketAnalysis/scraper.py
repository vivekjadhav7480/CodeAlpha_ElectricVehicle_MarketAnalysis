import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Website URL
url = "https://ev-database.org/"

# Request Headers
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Send Request
response = requests.get(url, headers=headers)

# Check Response
if response.status_code != 200:
    print("Failed to connect.")
    print("Status Code:", response.status_code)
    exit()

# Parse HTML
soup = BeautifulSoup(response.text, "lxml")

# List to store data
ev_data = []

# Find all EV cards
cars = soup.find_all("div", class_="list-item")

for car in cars:
    try:
        model = car.find("h2").get_text(strip=True)

        specs = car.find_all("div", class_="list-item-info")

        battery = ""
        ev_range = ""
        efficiency = ""

        if len(specs) >= 1:
            battery = specs[0].get_text(" ", strip=True)

        if len(specs) >= 2:
            ev_range = specs[1].get_text(" ", strip=True)

        if len(specs) >= 3:
            efficiency = specs[2].get_text(" ", strip=True)

        ev_data.append({
            "Model": model,
            "Battery": battery,
            "Range": ev_range,
            "Efficiency": efficiency
        })

    except Exception:
        continue

# Create dataset folder
os.makedirs("dataset", exist_ok=True)

# Save CSV
df = pd.DataFrame(ev_data)

df.to_csv("dataset/scraped_ev_data.csv", index=False)

print("===================================")
print("Web Scraping Completed Successfully")
print("===================================")
print(f"Total EVs Scraped : {len(df)}")
print(df.head())