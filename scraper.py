# scraper.py
import requests

def scrape_and_send():
    crash_values = [1.32, 1.47, 2.05, 1.32, 2.47]
    api_url = "https://aviator-bot-api.onrender.com/receive"
    try:
        res = requests.post(api_url, json={"values": crash_values})
        print(f"Sent crash values: {crash_values} | Status: {res.status_code}")
    except Exception as e:
        print("Error sending data:", e)

if __name__ == "__main__":
    scrape_and_send()
