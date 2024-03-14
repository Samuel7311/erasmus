import requests
import json
import time

def send_data_to_telegram():
    json_file = 'flucc/flucc/spiders/oFlucc.json'

    # Load JSON file
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        link = item['Link']
        event = item['Title']
        event_date = item['Date']

        message = f"Title: {event}\nDate: {event_date}\nLink: {link}"

        # Send message to Telegram
        response = requests.post(
             'https://api.telegram.org/bot7071671373:AAF0U60pGQTFOlkppeyaxkhXUbM-cs-1qdU/sendMessage',
            json={'chat_id': '-4176067898', 'text': message}
        )
        # Pause between sending messages
        time.sleep(1)

if __name__ == "__main__":
    send_data_to_telegram()
