# import socket
from socket import socket
import random
import sys

s = socket()

server_host = 'localhost'
server_port = 9999

try:
    s.connect((server_host, server_port))
except ConnectionRefusedError:
    print('El servidor no esta activo')
    print('Saliendo ...')
    sys.exit()

while True:
    r = str(random.randint(1, 3))
    res = str(s.recv(25))
    noJuegos = res[9]
    msg = f'C:[{res[3]}] DE:{noJuegos}|JJ:{res[14]}|RE:{r}'
    s.send(msg.encode())
    print(f'C:[{res[3]}] DE:{noJuegos}|JJ:{res[14]}|RE:{r}')

s.close()