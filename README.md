# Python-Chat-App
Creating a chat app using python. The chat app is able to support multiple clients on a single server and is able to help them communicate effectively. 

##Overview
My code has 2 files: server.py and client.py. First, we need to run the server file. After running, the server will show the output saying "Server is started". After that, we can run multiple client files using the command line. When the client.py file is run, the client is promoted to use a nickname and all it's subsequent messages will be sent in the room using that name. Further, as soon as the client chooses a name and gets connected to the server, a random color among the list of colors is assigned to the client and all the messages sent by that client will be in that color. Once a new client is  added to the cha, all the existing clients are notified. The server uses the client's IP Address and port number to connect with the client. Finally, the client can simply write ".exit" to exit from the app.
