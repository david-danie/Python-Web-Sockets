from re import M
from socket import socket
from threading import Thread, Lock
import time
import sys
MAX_JUEGOS = 5
# Se importa socket, Thread y time

socketServidor = socket()
host = 'localhost'
port = 9999
socketServidor.bind((host, port))
socketServidor.listen(5)
noConexiones = 0
resClientes = ['0', '0', '0']   # RespuestaC1, RespuestaC2, Resultado 
recordC1 = [0, 0, 0]            # Ganado, empatado, perdido
recordC2 = [0, 0, 0]            # Ganado, empatado, perdido
disponible = '0'
noConexiones = 0
noJuegos = 0

def hilo_imp():
    while True:
        time.sleep(5)
        if disponible == '1' and noJuegos < MAX_JUEGOS:
            if resClientes[0] == resClientes[1]:    # Si hay EMPATE
                resClientes[2] = '-'
                recordC1[1] += 1
                recordC2[1] += 1
            else:
                if resClientes[0] == '1' and resClientes[1] == '2': # 1=piedra 2=papel 3=tijera
                    resClientes[2] = 'x'
                    recordC1[2] += 1
                    recordC2[0] += 1
                elif resClientes[0] == '2' and resClientes[1] == '3': # Si perdió el Cliente 1
                    resClientes[2] = 'x'
                    recordC1[2] += 1
                    recordC2[0] += 1
                elif resClientes[0] == '3' and resClientes[1] == '1': # Si perdió el Cliente 1
                    resClientes[2] = 'x'
                    recordC1[2] += 1
                    recordC2[0] += 1
                else:                                                 # Si ganó el Cliente 1
                    resClientes[2] = '*'
                    recordC1[0] += 1
                    recordC2[2] += 1
                noJuegos += 1
        else:
            for i in recordC1:
                i = 0
            for i in recordC2:
                i = 0
            noJuegos = 0
        
        print(f'C1: {resClientes[0]}, G:{recordC1[0]} E:{recordC1[1]} P:{recordC1[2]} |'
              f' {noJuegos} | C2: {resClientes[1]}, G:{recordC2[0]} E:{recordC2[1]} P:{recordC2[2]}')

def hilo_cliente(sock, noCliente):

    msg = f'[{noCliente}] Recibido\n'
    sock.send(msg.encode())
    print(msg)

    salir = False
    #noJuegos = '0'
    disponible = '0'

    while not salir:
        resultado = resClientes[2]
        res = str(sock.recv(25))
        #print(res)
        resJuego = res[21]
        #noJuegos = res[16]
        
        if noConexiones == 2:
            disponible = '1'
        elif noConexiones == 1:
            disponible = '0'
            
        if noCliente == 2 and  resClientes[2] == 'x': # Invertir resultado a cliente 2
            resultado = '*' 
        elif noCliente == 2 and  resClientes[2] == '*': # Invertir resultado a cliente 2
            resultado = 'x'

        msg = f'[{noCliente}] DE:{disponible}|JJ:{noJuegos}|RE:{resJuego}|RS:{resultado}'
        sock.send(msg.encode())

        # if resJuego == '1':         # Pasa la respuesta a la lista resClientes
        #     resClientes[noCliente - 1] =  'piedra'    
        # elif resJuego == '2':
        #     resClientes[noCliente - 1] = 'papel'
        # else:
        #     resClientes[noCliente - 1] = 'tijera'
        resClientes[noCliente - 1] =  resJuego

        #print(f'Cliente[{res[4]}] selecciono {resClientes[noCliente - 1]}, en la ronda {noJuegos}.')
        time.sleep(5)

    sock.close()

if __name__ == '__main__':
    

    t3 = Thread(target = hilo_imp)
    t3.start()

    while True:
        print(f'Esperando conexion...')     
        try:
            conn, addr = socketServidor.accept()
        except:
            print('conexion no disponible')
            print('Saliendo ...')
            sys.exit()
        noConexiones += 1
        print(f'\n[{noConexiones}] Direccion: {addr}\n')
        t = Thread(target = hilo_cliente, args=(conn, noConexiones))
        t.start()