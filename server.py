import socket
import threading


# Connection Data
#Port is confidential thing
host = '127.0.0.1'                                                 #host IP address
port = 12347

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         #Creating a new socket
server.bind((host, port))                                          #Binding the socket to address.
server.listen()                                                    #Listening for connections made to the socket.

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Sending messages to the connected clients
def broadcast(message):
    for client in clients:
        client.send(message)                               #Sending data to the socket.

# Handling the messages from clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)                                      #broadcasting the message to everyone
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]                             #removing clients
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break


# Receiving the messages
def receive():
    try:
        while True:
            # Accept Connection
            client, address = server.accept()
            print("Connected with {}".format(str(address)))            #Waiting for new connections

            #Requesting and storing nickname

            client.send('NICK'.encode('ascii'))                        #Sending in encoded form
            nickname = client.recv(1024).decode('ascii')
            nicknames.append(nickname)
            clients.append(client)

            # Print And Broadcast Nickname
            #pritning
            print("Name is {}".format(nickname))
            #broadcasting
            broadcast("{} joined".format(nickname).encode('ascii'))   #informs when there's a new connection
            client.send('Connected to server!'.encode('ascii'))

            # handling the thread
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
    except:
        pass
print("Server is started ")
receive()