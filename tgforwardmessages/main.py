import os
import re

from telethon.sync import TelegramClient, events, utils
from common import API_ID, API_HASH, CHANNEL_READ_ID, CHANNEL_SEND_ID


session = os.environ.get("TG_SESSION", "Forwader")
client = TelegramClient(session, API_ID, API_HASH).start()


def parse_msg(msg):
    data = {}
    try:
        coin = re.findall("\S+(?=|)", msg, flags=re.IGNORECASE)[0]
    except:
        try:
            coin = re.findall("#\S+", msg, flags=re.IGNORECASE)[0]
            coin = coin.replace("#", "")
        except:
            print("COIN NOT IDENTIFIED")
            return None
    data["coin"] = coin

    try:
        direction = re.findall("LONG|SHORT", msg, flags=re.IGNORECASE)[0]
    except:
        print("direction NOT IDENTIFIED")
        return None
    data["direction"] = direction

    try:
        current_price = re.findall(
            "\d+.\d+(?!Current Price: )", msg, flags=re.IGNORECASE
        )[0]
    except:
        print("CURRENT PRICE NOT IDENTIFIED")
        return None
    data["current_price"] = current_price

    try:
        price_close = re.findall("price close \S+ \d+.\d+", msg, flags=re.IGNORECASE)[0]
        price_close = re.findall("\d+.\d+", price_close, flags=re.IGNORECASE)[0]
    except:
        print("COIN NOT IDENTIFIED")
        return None
    data["price_close"] = price_close
    return data


def main():
    print("Running")
    with client:
        print("Logged")

        @client.on(events.NewMessage(pattern="(?i).*Long|(?i).*Short"))
        async def handler(event):
            peer_channel = event.peer_id.stringify()
            try:
                channel_id = re.findall(
                    "[0-9]+(?!channel_id)", peer_channel, flags=re.IGNORECASE
                )[0]
            except:
                channel_id = 0

            if not channel_id == CHANNEL_READ_ID:
                return None

            sender = await event.get_sender()
            print("New MSG")
            data = parse_msg(event.text)
            if not data:
                return None

            stoploss = float(data["current_price"]) * 1.035
            takeprofit = float(data["current_price"]) * 0.965

            new_msg = (
                f"{data['coin']} \n"
                + f"Direction: {data['direction']} \n"
                + f"Leverage: Isolate 10x \n"
                + f"Entry: {data['current_price']} \n"
                + f"Stoploss: {stoploss} \n"
                + f"Takeprofit: {takeprofit}"
            )
            print(f"Se ha enviado el siguiente mensaje: \n{new_msg}")
            await client.send_message(CHANNEL_SEND_ID, new_msg)

        client.run_until_disconnected()


main()
