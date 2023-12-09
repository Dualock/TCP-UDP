import socket

def connect():
    # Client ip and port
    local_host = "127.0.0.1"
    port = 9999

    # Socket initialization, socket datagram
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 3 way handshake start
    client.sendto('Hello server'.encode('utf-8'), ((local_host, port)))
    data, server_address = client.recvfrom(1024)
    print(f"Respuesta del servidor: {data.decode('utf-8')}")
