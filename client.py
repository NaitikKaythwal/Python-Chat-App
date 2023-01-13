import socket, time, random
import threading
from colorama import Fore, init, Back
# init colors
init()

# set the available colors
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]

# choose a random color for the client
client_color = random.choice(colors)

print("Welcome to the Chat Room")
print('Connecting....')
# Choosing Nickname
time.sleep(1)
nickname = input("Enter you name: ")

# Connecting to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12347))  #connection to hostname on the port.

print("Connected!")


# Listening to server
def receive():
    while True:
        try:
            # Receiving messages
            message = client.recv(1024).decode("ascii")
                #client.close()
            word = ".exit"
            if word in message:
                print("Please press enter to leave the room")
                client.close()
                break

            if message == 'NICK':
                client.send(nickname.encode("ascii"))

            else:
                print(f"{message}")


        except:
            # Close connection if error
            print("An error occured!")
            client.close()
            break


# Sending messages
def write():
    while True:
        try:
            to_send = input()
            #message = '{}: {}'.format(nickname, input(''))
            message =  f"{client_color}{nickname}:{to_send}"
            client.send(message.encode("ascii"))
        except:
            # Closing the connection
            print("leaving the chat room")
            client.close()
            break


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()