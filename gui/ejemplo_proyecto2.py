
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
noJuegos = 0
respuesta = '1'
jugando = False

class QtWindow(QMainWindow):

    def __init__(self):

        super(QtWindow, self).__init__()
        self.ui = Ui_VENTANA_PRINCIPAL()
        self.ui.setupUi(self)

        self.ui.BOTONDEJUGAR.clicked.connect(self.botondejugar)
        self.ui.BOTONDECERRAR.clicked.connect(self.botondecerrar)
        self.ui.PIEDRA.clicked.connect(self.botonPiedra)
        self.ui.PAPEL.clicked.connect(self.botonPapel)
        self.ui.TIJERA.clicked.connect(self.botonTijera)
    
    # def get_respuesta(self):
    #     return self.respuesta 

    # def set_respuesta(self, r):
    #     self.respuesta = r
        
    def botondejugar(self):
        if respuesta == '0':
            print('Selecciona una opción')
        else:
            print('INICIA JUEGO')        
            msg = f'C[1]: DE:1|JJ:2|RE:{respuesta}'
            s.send(msg.encode())
            print(msg)
            #noJuegos =+ 1
        
    def botondecerrar(self):
        print('FIN DEL JUEGO')

    def botonPiedra(self):
        respuesta = '1'
        print('SELECCIONO PIEDRA')
        return respuesta
 
    def botonPapel(self):
        respuesta = '2'
        print('SELECCIONO PAPEL') 
        return respuesta

    def botonTijera(self):
        respuesta = '3'
        print('SELECCIONO TIJERA')
        return respuesta
    
try:
    s.connect((server_host, server_port))
except ConnectionRefusedError:
    print('El servidor no esta activo')
    print('Saliendo ...')
    sys.exit()

if __name__ == '__main__':

    app = QApplication()
    window = QtWindow()
    window.show()
    sys.exit(app.exec_())

