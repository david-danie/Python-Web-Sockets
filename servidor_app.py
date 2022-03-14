import time
from threading import Thread
from socket import socket
#import socket
import sys

# except ConnectionResetError:
#     print('Desconexion de clientes')
#     print('Saliendo ...')
#     sys.exit()

def trabajo(sock, tid):
    
    msg = f'[{tid}] Recibido'
    sock.send(msg.encode())
    print(msg)

    salir = False
    noJuegos = 0
    jDisponible = False
    respuesta = 0

    while not salir:

        if contador == 2:
            msg = f'[{tid}] J:{contador}|P:{noJuegos}|D:{jDisponible}|R:{respuesta}'
            
        elif contador == 1:
            msg = f'[{tid}] J:{contador}|P:{noJuegos}|D:{jDisponible}|R:{respuesta}'
        else:
            msg = f'[{tid}] Actualizacion'
        res = str(sock.recv(20))
        sock.send(msg.encode())
        print(msg + res)
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


# def trabajo(sock):
#     sock.send(b'recibido')
#     time.sleep(20)
#     sock.send(b'espera terminada')
#     sock.close()

# def sleeper(i):
#     print(f'Thread {i} espera {10-1} segundos')
#     time.sleep(10 - 2*1)
#     print(f'Thread - {i} termina')

# for i in range(10):
#     print(f'Creando Thread {i}')
#     t = Thread(target = sleeper, args = (i,))
#     t.start()

# print('Fin')