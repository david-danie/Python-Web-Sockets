
from socket import socket
from threading import Thread, Lock
from PySide2.QtWidgets import QApplication, QMainWindow
from PROYECTO_2 import Ui_VENTANA_PRINCIPAL
import sys, time

MAX_JUEGOS = 5

s = socket()
server_host = '18.211.34.177'
server_port = 3006
respuestaEnviar = ['0', '0', '0']
record = [0, 0, 0]
jugando = False

class QtWindow(QMainWindow):
    
    def __init__(self, respuesta, noJuegos):
        super(QtWindow, self).__init__()
        self.ui = Ui_VENTANA_PRINCIPAL()
        self.ui.setupUi(self)

        self.ui.BOTONDEJUGAR.clicked.connect(self.botondejugar)
        self.ui.BOTONDECERRAR.clicked.connect(self.botondecerrar)
        self.ui.PIEDRA.clicked.connect(self.botonPiedra)
        self.ui.PAPEL.clicked.connect(self.botonPapel)
        self.ui.TIJERA.clicked.connect(self.botonTijera)
        self.respuesta = respuesta
        self.noJuegos = noJuegos
        
    def botondejugar(self):
        if not self.respuesta == '0':
            if self.noJuegos < MAX_JUEGOS:
                msg = f'C[x]: DE:1|JJ:{self.noJuegos}|RE:{self.respuesta}'
                s.send(msg.encode())
                print(f'Mandaste tu respuesta: {msg}.') 
                self.noJuegos += 1
            else:
                self.noJuegos = 0
                print('Se reinició cuenta')                
        else:
            print('Selecciona una opción')
        
    def botondecerrar(self):
        print('FIN DEL JUEGO')

    def botonPiedra(self):
        self.respuesta = '1'
        print('Seleccionaste piedra')
 
    def botonPapel(self):
        self.respuesta = '2'
        print('Seleccionaste papel') 

    def botonTijera(self):
        self.respuesta = '3'
        print('Seleccionaste tijera')

try:
    s.connect((server_host, server_port))
except ConnectionRefusedError:
    print('El servidor no esta activo')
    print('Saliendo ...')
    sys.exit()

# def lee_servidor():
#     salir = False
#     while not salir:
#         res = s.recv(25).decode()
#         clientNo = res[4]
#         time.sleep(3)
#         print(res)

# th = Thread(target = lee_servidor)
# th.start()

if __name__ == '__main__':

    app = QApplication()
    window = QtWindow('0', 1)
    window.show()
    sys.exit(app.exec_())

