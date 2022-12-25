import socket

MAX_SIZE_BYTES = 65535

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f'The OS assigned address to me is {s.getsockname()}')
message = input('Input lowercase sentence: ')
data = message.encode('ascii')
s.sendto(data, ('127.0.0.1', 3000))

data, serverAddress = s.recvfrom(MAX_SIZE_BYTES)
text = data.decode('ascii')
print(f'The server {serverAddress} replied with {text}')