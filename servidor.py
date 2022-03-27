
from socket import socket
from threading import Thread, Lock
import time
import sys
# Se importa socket, Thread y time

MAX_JUEGOS = 5

socketServidor = socket()
host = 'localhost'
port = 9999
socketServidor.bind((host, port))
socketServidor.listen(5)
noConexiones = 0
resClientes = ['0', '0', '0']   # RespuestaC1, RespuestaC2, Resultado 
recordC1 = [0, 0, 0]            # Ganado, empatado, perdido
recordC2 = [0, 0, 0]            # Ganado, empatado, perdido
jugando = False
noConexiones = 0
noJuegos = 0
prueba = {'0':'0', '1':'Piedra', '2':'Papel', '3':'Tijera'}

def hilo_info():
    while True:
        time.sleep(5)
        if jugando == True and noJuegos < MAX_JUEGOS:
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
        
        print(f'C1: {prueba[resClientes[0]]} G:{recordC1[0]} E:{recordC1[1]} P:{recordC1[2]} |'
              f' {noJuegos} | C2: {prueba[resClientes[1]]}, G:{recordC2[0]} E:{recordC2[1]} P:{recordC2[2]}')

def hilo_cliente(sock, noCliente):

    msg = f'Cliente[{noCliente}] recibido.'
    sock.send(msg.encode())
    print(msg)

    salir = False

    while not salir:
        resultado = resClientes[2]
        res = str(sock.recv(25))

        resJuego = res[21]
        resClientes[noCliente - 1] =  resJuego
            
        if noCliente == 2 and  resClientes[2] == 'x': # Invertir resultado a cliente 2
            resultado = '*' 
        elif noCliente == 2 and  resClientes[2] == '*': # Invertir resultado a cliente 2
            resultado = 'x'

        msg = f'[{noCliente}] DE:0|JJ:{noJuegos}|RE:{resJuego}|RS:{resultado}'
        sock.send(msg.encode())
        #print(f'Cliente[{res[4]}] selecciono {resClientes[noCliente - 1]}, en la ronda {noJuegos}.')
        time.sleep(5)

    sock.close()

if __name__ == '__main__':

    t3 = Thread(target = hilo_info)
    t3.start()

    while True:
        print(f'Esperando conexion... ')     
        try:
            conn, addr = socketServidor.accept()
        except:
            print('Conexion no disponible')
            print('Saliendo ...')
            sys.exit()
        noConexiones += 1
        print(f'\n[{noConexiones}] Direccion: {addr}\n')
        t = Thread(target = hilo_cliente, args=(conn, noConexiones))
        t.start()