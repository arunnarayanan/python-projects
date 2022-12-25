import socket

MAX_SIZE_BYTES = 65535

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 3000
hostname = '127.0.0.1'
s.bind((hostname, port))
print(f'Listening at {s.getsockname()}')

while True:
    data, clientAddress = s.recvfrom(MAX_SIZE_BYTES)
    message = data.decode('ascii')
    uppperCaseMessage = message.upper()
    print(f'The client at {clientAddress} says {message}')
    data = uppperCaseMessage.encode('ascii')
    s.sendto(data, clientAddress)