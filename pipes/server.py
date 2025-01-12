import os
from pathlib import Path
from time import sleep

# Get the current working directory and append the path to the unix-sockets directory
root_dir = Path(__file__).parent
clientToServer = root_dir / 'client-to-server'
serverToClient = root_dir / 'server-to-client'

# If the client-to-server file does not exist, create it
if not clientToServer.exists():
    os.mkfifo(clientToServer)

# If the server-to-client file does not exist, create it
if not serverToClient.exists():
    os.mkfifo(serverToClient)

with open(clientToServer, 'r') as c2s:
    with open(serverToClient, 'w') as s2c:
        while True:
            message = c2s.readline()
            if not message:
                print('No more data received')
                break
            print('Received', message)
            # Sent "I received: " + data back to the client
            s2c.write('I received: ' + message + '\n')
            s2c.flush()
