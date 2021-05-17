import socket

sock = socket.socket()
sock.connect(('localhost', 8888))

def conv(data1):
    return data1.encode('utf-8')
def deconv(data1):
    return data1.decode('utf-8')

while True:
    a = input()
    sock.send(b''+conv(a))
    data = sock.recv(1024)
    print (deconv(data))
    
