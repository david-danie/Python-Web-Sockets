# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PROYECTO_2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VENTANA_PRINCIPAL(object):
    def setupUi(self, VENTANA_PRINCIPAL):
        if not VENTANA_PRINCIPAL.objectName():
            VENTANA_PRINCIPAL.setObjectName(u"VENTANA_PRINCIPAL")
        VENTANA_PRINCIPAL.resize(1088, 470)
        VENTANA_PRINCIPAL.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.BOTONDEJUGAR = QPushButton(VENTANA_PRINCIPAL)
        self.BOTONDEJUGAR.setObjectName(u"BOTONDEJUGAR")
        self.BOTONDEJUGAR.setGeometry(QRect(440, 330, 121, 41))
        self.BOTONDEJUGAR.setStyleSheet(u"font: 15 12pt \"Cambria\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 170, 255);")
        self.BOTONDECERRAR = QPushButton(VENTANA_PRINCIPAL)
        self.BOTONDECERRAR.setObjectName(u"BOTONDECERRAR")
        self.BOTONDECERRAR.setGeometry(QRect(440, 380, 121, 41))
        self.BOTONDECERRAR.setStyleSheet(u"font: 75 12pt \"Cambria\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 170, 255);")
        self.GANADOS = QLCDNumber(VENTANA_PRINCIPAL)
        self.GANADOS.setObjectName(u"GANADOS")
        self.GANADOS.setGeometry(QRect(30, 120, 81, 41))
        self.GANADOS.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.EMPATADOS = QLCDNumber(VENTANA_PRINCIPAL)
        self.EMPATADOS.setObjectName(u"EMPATADOS")
        self.EMPATADOS.setGeometry(QRect(30, 190, 81, 41))
        self.EMPATADOS.setStyleSheet(u"color: rgb(170, 170, 255);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 170, 255);")
        self.PERDIDOS = QLCDNumber(VENTANA_PRINCIPAL)
        self.PERDIDOS.setObjectName(u"PERDIDOS")
        self.PERDIDOS.setGeometry(QRect(30, 260, 81, 41))
        self.PERDIDOS.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.label = QLabel(VENTANA_PRINCIPAL)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 90, 51, 16))
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_2 = QLabel(VENTANA_PRINCIPAL)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 170, 81, 20))
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_3 = QLabel(VENTANA_PRINCIPAL)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 240, 71, 20))
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_4 = QLabel(VENTANA_PRINCIPAL)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 0, 631, 91))
        self.label_4.setStyleSheet(u"font: 75 20pt \"Cambria\";\n"
"background-color: rgb(170, 170, 255);")
        self.label_5 = QLabel(VENTANA_PRINCIPAL)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 330, 301, 91))
        self.label_5.setStyleSheet(u"font: 75 italic 12pt \"Cambria\";\n"
"background-color: rgb(170, 170, 255);")
        self.PIEDRA = QRadioButton(VENTANA_PRINCIPAL)
        self.PIEDRA.setObjectName(u"PIEDRA")
        self.PIEDRA.setGeometry(QRect(330, 340, 84, 19))
        self.PIEDRA.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.PAPEL = QRadioButton(VENTANA_PRINCIPAL)
        self.PAPEL.setObjectName(u"PAPEL")
        self.PAPEL.setGeometry(QRect(330, 370, 84, 19))
        self.PAPEL.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.TIJERA = QRadioButton(VENTANA_PRINCIPAL)
        self.TIJERA.setObjectName(u"TIJERA")
        self.TIJERA.setGeometry(QRect(330, 400, 84, 19))
        self.TIJERA.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.verticalLayoutWidget = QWidget(VENTANA_PRINCIPAL)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(170, 120, 291, 101))
        self.JUGADOR1 = QVBoxLayout(self.verticalLayoutWidget)
        self.JUGADOR1.setObjectName(u"JUGADOR1")
        self.JUGADOR1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_2 = QWidget(VENTANA_PRINCIPAL)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(520, 120, 281, 101))
        self.JUGADOR2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.JUGADOR2.setObjectName(u"JUGADOR2")
        self.JUGADOR2.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(VENTANA_PRINCIPAL)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 100, 121, 16))
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_7 = QLabel(VENTANA_PRINCIPAL)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(610, 100, 121, 16))
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.verticalLayoutWidget_3 = QWidget(VENTANA_PRINCIPAL)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(590, 350, 241, 71))
        self.MENSAJESDELSISTEMA = QVBoxLayout(self.verticalLayoutWidget_3)
        self.MENSAJESDELSISTEMA.setObjectName(u"MENSAJESDELSISTEMA")
        self.MENSAJESDELSISTEMA.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(VENTANA_PRINCIPAL)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(590, 330, 241, 16))
        self.label_8.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.verticalLayoutWidget_4 = QWidget(VENTANA_PRINCIPAL)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(170, 260, 631, 61))
        self.MENSAJESDELJUEGO = QVBoxLayout(self.verticalLayoutWidget_4)
        self.MENSAJESDELJUEGO.setObjectName(u"MENSAJESDELJUEGO")
        self.MENSAJESDELJUEGO.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(VENTANA_PRINCIPAL)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(340, 230, 281, 20))
        self.label_9.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.label_10 = QLabel(VENTANA_PRINCIPAL)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 40, 141, 41))
        self.label_10.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_11 = QLabel(VENTANA_PRINCIPAL)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(860, 40, 191, 171))
        self.label_11.setTextFormat(Qt.PlainText)
        self.label_11.setPixmap(QPixmap(u"img/IMAGEN_PROYECTO.jpg"))
        self.label_11.setScaledContents(True)
        self.label_12 = QLabel(VENTANA_PRINCIPAL)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(850, 260, 211, 141))
        self.label_12.setPixmap(QPixmap(u"img/CONTROL.jpg"))
        self.label_12.setScaledContents(True)

        self.retranslateUi(VENTANA_PRINCIPAL)

        QMetaObject.connectSlotsByName(VENTANA_PRINCIPAL)
    # setupUi

    def retranslateUi(self, VENTANA_PRINCIPAL):
        VENTANA_PRINCIPAL.setWindowTitle(QCoreApplication.translate("VENTANA_PRINCIPAL", u"Form", None))
#if QT_CONFIG(tooltip)
        VENTANA_PRINCIPAL.setToolTip(QCoreApplication.translate("VENTANA_PRINCIPAL", u"<html><head/><body><p align=\"center\"><span style=\" color:#55ffff;\"><br/></span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.BOTONDEJUGAR.setText(QCoreApplication.translate("VENTANA_PRINCIPAL", u"JUGAR", None))
        self.BOTONDECERRAR.setText(QCoreApplication.translate("VENTANA_PRINCIPAL", u"CERRAR", None))
        self.label.setText(QCoreApplication.translate("VENTANA_PRINCIPAL", u"GANADOS", None))
        self.label_2.setText(QCoreApplication.translate("VENTANA_PRINCIPAL", u"EMPATADOS", None))
        self.label_3.setText(QCoreApplication.translate("VENTANA_PRINCIPAL", u"PERDIDOS", None))
        self.label_4.setText(QCoreApplication.translate("VENTANA_PRINCIPAL", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#151515;\">PIEDRA, PAPEL O TIJERA</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("VENTANA_PRINCIPAL", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cambria'; font-size:12pt; font-weight:72; font-style:italic;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#070707;\">ELIGE UNA OPCION  Y </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#070707;\">PRECIONA EL BOTON DE JUGAR :3</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.PIEDRA.setToolTip(QCoreApplication.translate("VENTANA_PRINCIPAL", u"<html><head/><body><p><span style=\" font-weight:600;\">PIEDRA</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.PIEDRA.setText(QCoreApplication.translate("VENTANA_PRINCIPAL", u"PIEDRA", None))
        self.PAPEL.setText(QCoreApplication.translate("VENTANA_PRINCIPAL", u"PAPEL", None))
        self.TIJERA.setText(QCoreApplication.translate("VENTANA_PRINCIPAL", u"TIJERA", None))
        self.label_6.setText(QCoreApplication.translate("VENTANA_PRINCIPAL", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">JUGADOR 1</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("VENTANA_PRINCIPAL", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">JUGADOR 2</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("VENTANA_PRINCIPAL", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">MENSAJES DEL SISTEMA</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("VENTANA_PRINCIPAL", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#101010;\">MENSAJES DEL JUEGO</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("VENTANA_PRINCIPAL", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">RECORD!!</span></p></body></html>", None))
        self.label_11.setText("")
        self.label_12.setText("")
    # retranslateUi

