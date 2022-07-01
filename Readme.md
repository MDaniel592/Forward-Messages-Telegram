# Forward Messages in Telegram

The python code retrieves messages from Channel A, creates a new messages which is sent to Channel B
The idea was to parse each message from a specific channel (Channel A) creating a new message for a second channel (Channel B).

# Requirements
 - Docker
 - Telethon 1.24.0 (https://github.com/LonamiWebs/Telethon)

# Acciones
 - Introducir el API_ID, API_HASH,CHANNEL_READ_ID y CHANNEL_SEND_ID en common.py

# Comandos
 - Cuando hagas un cambio: docker-compose build 
 - Ejecutar el nuevo código: docker-compose up -d
 - Eliminar el contenedor (pararlo con intención de subir una nueva versión): docker-compose down