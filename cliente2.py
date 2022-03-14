# import socket
from socket import socket
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
# except ConnectionResetError:
#     print('El servidor se desconecto')
#     print('Saliendo ...')
#     sys.exit()

while True:
    res = str(s.recv(25))
    if res[3] == '2':
        t1 = 'disponible, manda tu respuesta'
    else:
        t1 = 'no disponible'
    print(f'Servidor:{res}')
    print(f'Soy cliente:[{res[3]}]. Juego {t1}.')

    msg = f'J:{res[8]}|JJ:Pie'
    s.send(msg.encode())


s.close()