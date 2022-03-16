import time
from threading import Thread
from socket import socket
#import socket
import sys

def trabajo(sock, tid):
    
    msg = f'[{tid}] Recibido'
    sock.send(msg.encode())
    print(msg)

    salir = False
    noJuegos = 0
    jDisponible = '0'

    while not salir:
        res = str(sock.recv(25))
        resJuego = res[21]
        if contador == 2:
            jDisponible = '1'
            msg = f'[{tid}] DE:{jDisponible}|JJ:{noJuegos}|RE:{resJuego}'      
        elif contador == 1:
            jDisponible = '0'
            msg = f'[{tid}] DE:{jDisponible}|JJ:{noJuegos}|RE:{resJuego}'
        #   tid*4 jdis*9 noju*14 res*19
        else:
            msg = f'[{tid}] En espera'

        sock.send(msg.encode())
        print(msg)
        time.sleep(5)

    sock.close()

s = socket()
host = 'localhost'
port = 9999
s.bind((host, port))
s.listen(5)
contador = 0



while True:
    print('Esperando conexion')
    conn, addr = s.accept()
    contador += 1
    print(f'[{contador}] Direccion: {addr}')
    t = Thread(target=trabajo, args=(conn, contador))
    t.start()