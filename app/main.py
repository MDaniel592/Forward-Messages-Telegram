import logging
import os
import re

from telethon.sync import TelegramClient, events
from common import API_ID, API_HASH, CHANNEL_READ_ID, CHANNEL_SEND_ID, ALLOWED_MESSAGES

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

session = os.environ.get("TG_SESSION", "Forwader")
client = TelegramClient(session, API_ID, API_HASH).start()


def main():
    logger.warning("Running")
    with client:
        logger.warning("Logged")

        @client.on(events.NewMessage())
        async def handler(event):
            peer_channel = event.peer_id.stringify()
            try:
                channel_id = int(
                    re.findall(
                        "[0-9]+(?!channel_id)", peer_channel, flags=re.IGNORECASE
                    )[0]
                )
            except:
                channel_id = 0

            logger.warning(f"Mensaje recibido del canal con ID: {channel_id}")
            if not channel_id == CHANNEL_READ_ID:
                return None

            sender = await event.get_sender()
            msg = event.text
            valid = re.findall(ALLOWED_MESSAGES, msg, re.IGNORECASE)
            if not valid:
                return None

            new_msg = msg + "\n**Leverage: 10x isolate**"
            logger.warning(f"Se ha enviado el siguiente mensaje: \n{new_msg}")
            await client.send_message(entity=CHANNEL_SEND_ID, message=new_msg)

        client.run_until_disconnected()


main()
