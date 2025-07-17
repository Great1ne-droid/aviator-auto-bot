# scraper.py

import requests
import json

def scrape_and_send():
    # Dummy crash values for testing
    crash_values = [1.32, 1.47, 2.05, 1.32, 2.47]
    
    # Make sure this matches your actual Render web service endpoint
    api_url = "https://aviator-bot-api.onrender.com/receive"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "values": crash_values
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        print(f"Status code: {response.status_code}")
        print("Response:", response.text)
    except Exception as e:
        print("Failed to send crash data:", e)

if __name__ == "__main__":
    scrape_and_send()
