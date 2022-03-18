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
    noJuegos = '0'
    disponible = '0'

    while not salir:
        res = str(sock.recv(25))
        resJuego = res[21]
        
        if contador == 2:
            disponible = '1'
            #msg = f'[{tid}] DE:{disponible}|JJ:{noJuegos}|RE:{resJuego}'      
        elif contador == 1:
            disponible = '0'
            #msg = f'[{tid}] DE:{disponible}|JJ:{noJuegos}|RE:{resJuego}'
        #   tid*4 jdis*9 noju*14 res*19
        else:
            msg = f'[{tid}] En espera'
            
        msg = f'[{tid}] DE:{disponible}|JJ:{noJuegos}|RE:{resJuego}'
        sock.send(msg.encode())

        if resJuego == '1':
            t1 = 'piedra'    
        elif resJuego == '2':
            t1 = 'papel'
        else:
            t1 = 'tijera'
        print(f'El cliente [{res[4]}] ha seleccionado {t1}, en la ronda {noJuegos}.')
        time.sleep(5)

    sock.close()

s = socket()
host = 'localhost'
port = 9999
s.bind((host, port))
s.listen(5)
contador = 0

if __name__ == '__main__':

    while True:
        print('Esperando conexion')
        conn, addr = s.accept()
        contador += 1
        print(f'[{contador}] Direccion: {addr}')
        t = Thread(target=trabajo, args=(conn, contador))
        t.start()