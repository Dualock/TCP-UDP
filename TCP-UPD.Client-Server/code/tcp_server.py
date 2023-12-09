import socket


def handshake(client, address):
    # Receive sync request
    print(f"Connected to {address} ")
    SYN = client.recv(1024).decode('utf-8')
    print("received: ", SYN)

    # Sending ACK to the client
    print('Sending ACK')
    client.send("ACK".encode('utf-8'))

    ACK = client.recv(1024).decode('utf-8')
    print("Received: ", ACK)


def sendResponse(message, client):
    client.send(message.encode('utf-8'))


def run_server():
    # Server IP and port configuration
    local_host = '127.0.0.1'
    port = 9999

    # Socket initialization
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((local_host, port))

    #Port listening
    server.listen()
    print(f'Waiting for client to connect {local_host}:{port}')

    #Accept connection
    client, address = server.accept()
    handshake(client, address)
    while (True):
        # Receive lowercase message
        message = client.recv(1024).decode('utf-8')
        print("Received: ", message)

        # If client ends the connection, terminate the loop
        if(message == 'disconnect'):
            client.close()
            server.close()
            break
        else:
            # Converting to Upper case
            message = message.upper()
            #Sending to the client
            sendResponse(message, client)

        
        # Disconnect
        
