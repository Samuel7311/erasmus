import requests
import json
import time
from datetime import date


def daswerk():
    json_file = 'daswerk/erasmus/spiders/oDaswerk.json'

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    global today
    today = date.today()
    today_string = today.strftime("%d-%m-%Y")

    for item in data:
        link = item['Link']
        event = item['Title']
        event_date = item['Date']

        year = event_date[-4:]
        month = event_date[-9:-6]
        day = event_date[-24:-22]

        month_mapping = {
            'Jan': '01',
            'Feb': '02',
            'Mär': '03',
            'Apr': '04',
            'Mai': '05',
            'Jun': '06',
            'Jul': '07',
            'Aug': '08',
            'Sep': '09',
            'Okt': '10',
            'Nov': '11',
            'Dez': '12'
        }
        month_abbreviation = (month)
        month_number = month_mapping.get(month_abbreviation)

        together = day + "-" + month_number + "-" + year

        if today_string == together:
            message = f"Title: {event}\nDate: {event_date}\nLink: {link}"

            # Send message to Telegram
            response = requests.post(
                'https://api.telegram.org/bot7071671373:AAF0U60pGQTFOlkppeyaxkhXUbM-cs-1qdU/sendMessage',
                json={'chat_id': '-4176067898', 'text': message}
            )
            # Pause between sending messages
            time.sleep(1)


def flex():
    json_file = 'flex/flex/spiders/oFlex.json'

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    global today
    today = date.today()
    today_string = today.strftime("%d-%m-%Y")

    for item in data:
        link = item['Link']
        event = item['Title']
        event_date = item['Date']

        year = "2024"
        month = event_date[-17:-14]
        day = event_date[-20:-18]

        month_mapping = {
            'Jan': '01',
            'Feb': '02',
            'Mrz': '03',
            'Apr': '04',
            'May': '05',
            'Jun': '06',
            'Jul': '07',
            'Aug': '08',
            'Sep': '09',
            'Oct': '10',
            'Nov': '11',
            'Dec': '12'
        }
        month_abbreviation = (month)

        month_number = month_mapping.get(month_abbreviation)

        together = day + "-" + month_number + "-" + year

        if today_string == together:
            message = f"Title: {event}\nDate: {event_date}\nLink: {link}"

            # Send message to Telegram
            response = requests.post(
                'https://api.telegram.org/bot7071671373:AAF0U60pGQTFOlkppeyaxkhXUbM-cs-1qdU/sendMessage',
                json={'chat_id': '-4176067898', 'text': message}
            )
            # Pause between sending messages
            time.sleep(1)


def flucc():
    json_file = 'flucc/flucc/spiders/oFlucc.json'

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    global today
    today = date.today()
    today_string = today.strftime("%d-%m-%Y")

    for item in data:
        link = item['Link']
        event = item['Title']
        event_date = item['Date']

        year = event_date[-4:]
        month = event_date[-8:-5]
        day = event_date[-12:-10]

        month_mapping = {
            'Jan': '01',
            'Feb': '02',
            'Mär': '03',
            'Apr': '04',
            'Mai': '05',
            'Jun': '06',
            'Jul': '07',
            'Aug': '08',
            'Sep': '09',
            'Okt': '10',
            'Nov': '11',
            'Dez': '12'
        }
        month_abbreviation = (month)

        month_number = month_mapping.get(month_abbreviation)

        together = day + "-" + month_number + "-" + year

        if today_string == together:
            message = f"Title: {event}\nDate: {event_date}\nLink: {link}"

            # Send message to Telegram
            response = requests.post(
                'https://api.telegram.org/bot7071671373:AAF0U60pGQTFOlkppeyaxkhXUbM-cs-1qdU/sendMessage',
                json={'chat_id': '-4176067898', 'text': message}
            )
            # Pause between sending messages
            time.sleep(1)


def goabase():
    json_file = 'goabase/goabase/spiders/oGoabase.json'

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    global today
    today = date.today()
    today_string = today.strftime("%d-%m-%Y")

    for item in data:
        link = item['Link']
        event = item['Title']
        event_date = item['Date']

        year = event_date[-9:-7]
        month = event_date[-13:-10]
        day = event_date[-16:-14]

        month_mapping = {
            'Jan': '01',
            'Feb': '02',
            'Mar': '03',
            'Apr': '04',
            'May': '05',
            'Jun': '06',
            'Jul': '07',
            'Aug': '08',
            'Sep': '09',
            'Oct': '10',
            'Nov': '11',
            'Dec': '12'
        }
        month_abbreviation = (month)

        month_number = month_mapping.get(month_abbreviation)

        together = day + "-" + month_number + "-20" + year

        if today_string == together:
            message = f"Title: {event}\nDate: {event_date}\nLink: {link}"

            # Send message to Telegram
            response = requests.post(
                'https://api.telegram.org/bot7071671373:AAF0U60pGQTFOlkppeyaxkhXUbM-cs-1qdU/sendMessage',
                json={'chat_id': '-4176067898', 'text': message}
            )
            # Pause between sending messages
            time.sleep(1)


def goodnight():
    json_file = 'goodnight/goodnight/spiders/oGoodnight.json'

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    global today
    today = date.today()
    today_string = today.strftime("%d-%m-%Y")

    for item in data:
        link = item['Link']
        event = item['Title']
        event_date = item['Date']

        year = event_date[-2:]
        month = event_date[-4]
        day = event_date[-7:-5]
        together = day + "-0" + month + "-20" + year

        if today_string == together:
            message = f"Title: {event}\nDate: {event_date}\nLink: {link}"

            # Send message to Telegram
            response = requests.post(
                'https://api.telegram.org/bot7071671373:AAF0U60pGQTFOlkppeyaxkhXUbM-cs-1qdU/sendMessage',
                json={'chat_id': '-4176067898', 'text': message}
            )
            # Pause between sending messages
            time.sleep(1)


if __name__ == "__main__":
    daswerk()
    flex()
    flucc()
    goabase()
    goodnight()