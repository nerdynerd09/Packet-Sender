import socket
import ssl

# hostname = 'http://b3e3-103-224-54-104.ngrok.io'
hostname = '138.197.192.84'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())
        print(ssock.getsockname())
        print(ssock.getpeername())
        print(ssock.recv(1024))