
from socket import socket
from PySide2.QtWidgets import QApplication, QMainWindow
from PROYECTO_2 import Ui_VENTANA_PRINCIPAL
import sys

MAX_JUEGOS = 5

s = socket()
server_host = 'localhost'
server_port = 9999
respuestaEnviar = ['0', '0', '0']
record = [0, 0, 0]
#noJuegos = 0
#respuesta = '0'
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
    
    # def get_respuesta(self):
    #     return self.respuesta 

    # def set_respuesta(self, r):
    #     self.respuesta = r
        
    def botondejugar(self):
        if not self.respuesta == '0':
            if self.noJuegos < MAX_JUEGOS:
                msg = f'C[1]: DE:1|JJ:{self.noJuegos}|RE:{self.respuesta}'
                s.send(msg.encode())
                print(msg)
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
        print('SELECCIONÓ PIEDRA')
 
    def botonPapel(self):
        self.respuesta = '2'
        print('SELECCIONÓ PAPEL') 

    def botonTijera(self):
        self.respuesta = '3'
        print('SELECCIONÓ TIJERA')
    def manda_info():
        ...
    
try:
    s.connect((server_host, server_port))
except ConnectionRefusedError:
    print('El servidor no esta activo')
    print('Saliendo ...')
    sys.exit()

if __name__ == '__main__':

    app = QApplication()
    window = QtWindow('0', 1)
    window.show()
    sys.exit(app.exec_())

