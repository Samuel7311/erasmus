import requests
import json
import time
def send_data_to_telegram():
    with open('flucc/flucc/spiders/oFlucc.json', "r", encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            link = item['Link']
            event = item['Event']
            date = item['Date']

            # Construct message
            message = f"Event: {event}\nDate: {date}\nLink: {link}"

            # Send message to Telegram
            response = requests.post(
                'https://api.telegram.org/bot7071671373:AAF0U60pGQTFOlkppeyaxkhXUbM-cs-1qdU/sendMessage',
                json={'chat_id': '-4176067898', 'text': message}
            )

            # Rewrite JSON file without processed line
            with open('flucc/flucc/spiders/oFlucc.json', "w", encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=4)

            # Pause between sending messages
            time.sleep(2)

if __name__ == "__main__":
    send_data_to_telegram()

    
