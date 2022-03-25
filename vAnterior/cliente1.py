# import socket
from socket import socket
import random
import sys
MAX_JUEGOS = 5

s = socket()
server_host = 'localhost'
server_port = 9999
respuestaEnviar = ['0', '0', '0']
record = [0, 0, 0]
noJuegos = 0

try:
    s.connect((server_host, server_port))
except ConnectionRefusedError:
    print('El servidor no esta activo')
    print('Saliendo ...')
    sys.exit()

while True:
    r = str(random.randint(1, 3))
    res = str(s.recv(30))
    if res[9] == '1' and noJuegos < MAX_JUEGOS:
        if res[24] == '-':
            record[1] += 1
        elif res[24] == 'x':
            record[2] += 1
        elif res[24] == '*':
            record[0] += 1
        noJuegos += 1
    else:
        noJuegos = 0
        record[0] = 0
        record[1] = 0
        record[2] = 0
    msg = f'C[{res[3]}]: DE:{noJuegos}|JJ:{res[14]}|RE:{r}'
    #msg = respuestaEnviar
    s.send(msg.encode())
    print(msg)
    print(f'Ganados: {record[0]}. Empatados: {record[1]}. Perdidos: {record[2]}.')

s.close()