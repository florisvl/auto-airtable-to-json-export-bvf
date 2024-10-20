import os
import requests
import json
from dotenv import load_dotenv

# Laad omgevingsvariabelen
load_dotenv()

AIRTABLE_API_KEY = os.getenv('AIRTABLE_API_KEY')
AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID')
AIRTABLE_TABLE_NAME = os.getenv('AIRTABLE_TABLE_NAME')

# Airtable API URL
url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"

# Headers voor de API-aanroep
headers = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}"
}

# Functie om data op te halen en op te slaan als JSON
def fetch_and_save_data():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Data vernieuwd en opgeslagen als data.json")
    else:
        print(f"Error {response.status_code}: {response.text}")

# Haal de data op en sla het op
if __name__ == "__main__":
    fetch_and_save_data()