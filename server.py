import sys
import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 4444
logname = 'logs.txt'

sock.bind((host, port))
sock.listen(1)

while True:
    c, addr = sock.accept()

    while True:
        command = input('> ')
        c.send(command.encode())

        with open(logname, 'w+') as f:
            data = c.recv(65535).decode()
            f.write(data)
            print(data)
    c.close()
s.close()