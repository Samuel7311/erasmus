import requests
import json
import time
from datetime import date

def send_data_to_telegram():
    # List of JSON files
    json_files = ['daswerk/erasmus/spiders/oDaswerk.json', 'flex/flex/spiders/oFlex.json',
                  'flucc/flucc/spiders/oFlucc.json', 'goabase/goabase/spiders/oGoabase.json',
                  'goodnight/goodnight/spiders/oGoodnight.json']

    for json_file in json_files:
        # Load JSON file
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

    global today
    today = date.today()
    today_string = today.strftime("%d-%m-%Y")

    for item in data:
        link = item['Link']
        event = item['Title']
        event_date = item['Date']

        print(event_date)

        if today_string == event_date:
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



