import os
from pathlib import Path

# Get the current working directory and append the path to the unix-sockets directory
root_dir = Path(__file__).parent
clientToServer = root_dir / 'client-to-server'
serverToClient = root_dir / 'server-to-client'

with open(clientToServer, 'w') as c2s:
    with open(serverToClient, 'r') as s2c:
        c2s.write('Here comes my custom message\n')
        c2s.flush()
        print('Received', s2c.readline()) # When this line gets moved here, the program blocks. But the server has sendet two messages. Why?
        message = input('Enter your message: ') #                      | 
        c2s.write(message + '\n') #                                    |
        c2s.flush() #                                                  |
        # <-------------------------------------------------------------
        print('Received', s2c.readline())
        