# Forward Messages in Telegram

The python code retrieves messages from Channel A, creates a new messages which is sent to Channel B.
The idea was to parse each message from a specific channel (Channel A) creating a new message for a second channel (Channel B).

# Requirements
 - Docker
 - Docker-compose
 - Telethon 1.24.0 (https://github.com/LonamiWebs/Telethon)

# Acciones
 - Introducir el API_ID, API_HASH,CHANNEL_READ_ID y CHANNEL_SEND_ID en common.py

# Configuración inicial
Crear una nueva sesión válida de Telegram
 1. Ejecutar pip3 install -r requirements
 2. Ejecutar main (python3 main.py)
 3. Completar con tú número de móvil y el código recibido
 4. Cerrar la ventana
 5. Asegurarse de mover el fichero 'Forwader.session' dentro de la carpeta 'app'

# Una vez completada la configuración original, se puede crear un contenedor Docker
## Comandos docker
 - Cuando hagas un cambio: docker-compose build 
 - Ejecutar el nuevo código: docker-compose up -d
 - Eliminar el contenedor (pararlo con intención de subir una nueva versión): docker-compose down