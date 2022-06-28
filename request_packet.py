import socket
import ssl

context = ssl.create_default_context()

# host = "127.0.0.1"
host = "google.com"
port = 80
# port = 4444

def tcp(host,port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host,port))
    fromIP = client.getsockname()[0]
    fromPort = client.getsockname()[1]
    # client.send(b'GET / HTTP1.1\r\nHost: www.google.com\r\n\r\n')
    client.send((f'GET / HTTP/1.1\r\nHost: www.{host}\r\n\r\n').encode('utf-8'))    
    response = client.recv(4096)
    asciiResponse = response.decode()
    hexResponse = response.hex()
    # print('\n\n\n\n')
    # print(response.hex())
    return fromIP,fromPort,asciiResponse,hexResponse


# Run `nc -ul -p 4444` to verify udp connection
def udp(host,port):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # print(client.getpeername())
    # fromIP = client.getsockname()[0]
    # fromPort = client.getsockname()[1]
    client.sendto(b"Hello Aditi",(host,port))
    response = client.recv(4096)
    client.close()
    asciiResponse = response.decode()
    hexResponse = response.hex()    
    # print(fromIP)
    # return fromIP,fromPort,asciiResponse,hexResponse

def ssl(host,port):
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            print(ssock.version())
            print(ssock.getsockname())
            print(ssock.getpeername())
            print(ssock.recv(1024))

def httpGet(host):
    port = 80
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host,port))
    fromIP = client.getsockname()[0]
    fromPort = client.getsockname()[1]
    # client.send(b'GET / HTTP1.1\r\nHost: www.google.com\r\n\r\n')
    client.send((f'GET / HTTP/1.1\r\nHost: www.{host}\r\n\r\n').encode('utf-8'))    
    response = client.recv(4096)
    asciiResponse = response.decode()
    hexResponse = response.hex()
    # print('\n\n\n\n')
    # print(response.hex())
    return fromIP,fromPort,asciiResponse,hexResponse

def httpsGet(host):
    port = 443
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host,port))
    fromIP = client.getsockname()[0]
    fromPort = port
    # client.send(b'GET / HTTP1.1\r\nHost: www.google.com\r\n\r\n')
    client.send((f'GET / HTTPS/1.1\r\nHost: www.{host}\r\n\r\n').encode('utf-8'))    
    response = client.recv(4096)
    asciiResponse = response.decode()
    hexResponse = response.hex()
    # print('\n\n\n\n')
    print(response.hex())
    print(fromIP,fromPort,asciiResponse,hexResponse)
    # return fromIP,fromPort,asciiResponse,hexResponse

def httpPost(host,path,data):
    data = data
    dataLength = len(data)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host,80))
    fromIP = client.getsockname()[0]
    fromPort = client.getsockname()[1]
    # client.send(b'GET / HTTP1.1\r\nHost: www.google.com\r\n\r\n')
    client.send((f'POST /{path} HTTP/1.1\r\nHost: www.{host}\r\n\r\nContent-Length: {dataLength}\n\n{data}').encode('utf-8'))    
    response = client.recv(4096)
    asciiResponse = response.decode()
    hexResponse = response.hex()
    print(asciiResponse)
    # print(response.hex())
    return fromIP,fromPort,asciiResponse,hexResponse

def httpsPost(host,path,data):
    data =data
    dataLength = len(data)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host,443))
    fromIP = client.getsockname()[0]
    fromPort = client.getsockname()[1]
    # client.send(b'GET / HTTP1.1\r\nHost: www.google.com\r\n\r\n')
    client.send((f'POST /{path} HTTP/1.1\r\nHost: www.{host}\r\n\r\nContent-Length: {dataLength}\n\n{data}').encode('utf-8'))    
    response = client.recv(4096)
    asciiResponse = response.decode()
    hexResponse = response.hex()
    print(asciiResponse)
    # print(response.hex())
    return fromIP,fromPort,asciiResponse,hexResponse

# ssl("138.197.192.84",443)
# tcp(host=host,port=port)
udp(host="192.168.1.33",port=4444)
# httpPost("httpbin.org","post","another=value&param=with")
# httpsPost("httpbin.org","post","another=value&param=with")
# httpsGet("google.com")