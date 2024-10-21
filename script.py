import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

# Ophaalgegevens voor Tabel 1
AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_TABLE_NAME_1 = os.getenv("AIRTABLE_TABLE_NAME_1")
AIRTABLE_TABLE_NAME_2 = os.getenv("AIRTABLE_TABLE_NAME_2")

headers = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}",
    "Content-Type": "application/json"
}

# Haal gegevens op van Tabel 1
url1 = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME_1}"
response1 = requests.get(url1, headers=headers)

if response1.status_code == 200:
    data1 = response1.json()
    with open('data-table1.json', 'w') as f:
        json.dump(data1, f, indent=4)
    print("Tabel 1 data vernieuwd en opgeslagen als data-table1.json")
else:
    print(f"Error {response1.status_code}: {response1.text}")

# Haal gegevens op van Tabel 2
url2 = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME_2}"
response2 = requests.get(url2, headers=headers)

if response2.status_code == 200:
    data2 = response2.json()
    with open('data-table2.json', 'w') as f:
        json.dump(data2, f, indent=4)
    print("Tabel 2 data vernieuwd en opgeslagen als data-table2.json")
else:
    print(f"Error {response2.status_code}: {response2.text}")