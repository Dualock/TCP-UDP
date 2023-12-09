import socket

def connect():
    # Client ip and port
    local_host = "127.0.0.1"
    port = 9999

    # Socket initialization, socket datagram
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 3 way handshake start
    client.connect((local_host, port))
    print("sending SYN to the server")
    client.send("SYN request".encode('utf-8'))

    # Waiting for the ACK
    data = client.recv(1024).decode('utf-8')
    print(f"Receive message: {data}")

    # Sending ACK to the server
    message = "Handshake completed!".encode('utf-8')
    print("Sending Ack")
    client.send(message)

    # Sending a message
    message = input("Send a lowercase message to the server: ")
    print("Sending: ", message)
    encoded_message = message.encode('utf-8')
    client.send(encoded_message)

    data = client.recv(1024).decode('utf-8')
    print("receive message:", data)

    # Disconnect
    client.close()
