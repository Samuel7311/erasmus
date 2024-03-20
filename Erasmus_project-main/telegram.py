import asyncio
from telethon import TelegramClient
import json

api_id = "10231041"
api_hash = "ce4b7e036cf00173b83874dccf07fc8c"
bot_token = "7071671373:AAF0U60pGQTFOlkppeyaxkhXUbM-cs-1qdU"

group_name = -4176067898

async def send_new_events():
    # Load the list of sent event titles
    try:
        with open('sent_events.json', 'r') as file:
            sent_event_titles = set(json.load(file))
    except FileNotFoundError:
        sent_event_titles = set()

    # Create a new TelegramClient instance for the bot
    bot_client = TelegramClient('bot_session', api_id, api_hash)
    await bot_client.start(bot_token=bot_token)

    group = await bot_client.get_entity(group_name)

    # Load events from the JSON file
    with open('flucc/flucc/spiders/oFlucc.json', 'r') as file:
        events = json.load(file)

    for event in events:
        if event['Title'] in sent_event_titles:
            continue  # Skip sending the event if already sent

        # Construct the message for the event
        message = f"Title: {event['Title']}\nDate: {event['Date']}\nLink: {event['Link']}"

        # Send the message to the Telegram group
        await bot_client.send_message(group, message)

        # Update the list of sent event titles
        sent_event_titles.add(event['Title'])

    # Save the updated list of sent event titles
    with open('sent_events.json', 'w') as file:
        json.dump(list(sent_event_titles), file)

    await bot_client.disconnect()

asyncio.run(send_new_events())