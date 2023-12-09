import socket

def run_server():
    # Server IP and port configuration
    local_host = '127.0.0.1'
    port = 9999

    # Socket initialization, socket datagram
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((local_host, port))

    # Receive 1024 bytes of data
    message, address = server.recvfrom(1024)
    message = message.decode('utf-8')

    #20 bytes of IP header + 8 bytes of UDP header UDP
    datagram_size = len(message) + 28  
    print(f"From {address}: {message}, Datagram size {datagram_size} bytes")
    server.sendto('Hello Client,'.encode('utf-8').upper(), address)



