import requests
import json
from datetime import datetime, timedelta

# PRH API: Kuulutukset (Konkurssit)
# Tässä haetaan viimeisen 30 päivän kuulutukset
date_limit = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
API_URL = f"https://avoindata.prh.fi/bis/v1/announcements?maxResults=100&announcementType=KONKURSSI&entryDateFrom={date_limit}"

def fetch_konkurssit():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json().get('results', [])
        # Tallennetaan JSON-tiedostoon GitHub Pagesia varten
        with open('konkurssit.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Haettu {len(data)} ilmoitusta.")
    else:
        print("Virhe PRH:n rajapinnassa.")

if __name__ == "__main__":
    fetch_konkurssit()
