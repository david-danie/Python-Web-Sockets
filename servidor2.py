from socket import socket
from threading import Thread, Lock
import time
import sys
# Se importa socket, Thread y time

socketServidor = socket()
host = 'localhost'
port = 9999
socketServidor.bind((host, port))
socketServidor.listen(5)
noConexiones = 0
resClientes = ['0', '0']

noConexiones = 0
def hilo_imp():
    while True:
        time.sleep(5)
        #print(f'C1: {resClientes[0]} | C2: {resClientes[1]}.')
        if resClientes[0] == resClientes[1]:
            print('Empate!')
        else:
            if resClientes[0] == '1' and resClientes[1] == '2':
                print('Gano 2')
            elif resClientes[0] == '2' and resClientes[1] == '3':
                print('Gano 2')
            elif resClientes[0] == '3' and resClientes[1] == '1':
                print('Gano 2')
            else:
                print('Gano 1')
        print(f'C1: {resClientes[0]} | C2: {resClientes[1]}.')

def hilo_cliente(sock, noCliente):

    msg = f'[{noCliente}] Recibido'
    sock.send(msg.encode())
    print(msg)

    salir = False
    noJuegos = '0'
    disponible = '0'

    while not salir:
        res = str(sock.recv(25))
        resJuego = res[21]
        
        if noConexiones == 2:
            disponible = '1'
        elif noConexiones == 1:
            disponible = '0'
        else:
            msg = f'[{noCliente}] En espera'
            
        msg = f'[{noCliente}] DE:{disponible}|JJ:{noJuegos}|RE:{resJuego}'
        sock.send(msg.encode())

        if resJuego == '1':
            resClientes[noCliente - 1] = resJuego
            t1 = 'piedra'    
        elif resJuego == '2':
            resClientes[noCliente - 1] = resJuego
            t1 = 'papel'
        else:
            resClientes[noCliente - 1] = resJuego
            t1 = 'tijera'
        print(f'Cliente[{res[4]}] selecciono {t1}, en la ronda {noJuegos}.')
        time.sleep(5)

    sock.close()

if __name__ == '__main__':
    
    # print('dn')
    # time.sleep(3)
    t3 = Thread(target = hilo_imp)
    t3.start()
    while True:
        print(f'Esperando conexion. C1: {resClientes[0]} | C2: {resClientes[1]}.')
        try:
            conn, addr = socketServidor.accept()
        except:
            print('conexion no disponible')
            print('Saliendo ...')
            sys.exit()
        noConexiones += 1
        print(f'[{noConexiones}] Direccion: {addr}')
        t = Thread(target = hilo_cliente, args=(conn, noConexiones))
        t.start()