from PyQt5 import QtWidgets, uic, QtCore
from Segundo_Parcial.Regresion_lineal.Caso_de_prueba_1 import CasoPrueba1
from Segundo_Parcial.Regresion_lineal.Caso_de_prueba_2 import CasoPrueba2
from Segundo_Parcial.Regresion_lineal.Caso_de_prueba_3 import CasoPrueba3
from Segundo_Parcial.Regresion_lineal.Caso_de_prueba_4 import CasoPrueba4

class VentanaRegresion(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_regresion_lineal.ui", self)
        self.show()

        self.pushButton.clicked.connect(self.botonPrueba1Click)
        self.pushButton_2.clicked.connect(self.botonPrueba2Click)  
        self.pushButton_3.clicked.connect(self.botonPrueba3Click)
        self.pushButton_4.clicked.connect(self.botonPrueba4Click)        

    def botonPrueba1Click(self):
        casoprueba1 = CasoPrueba1()
        casoprueba1.leerDatos()
        casoprueba1.RealizarCalculo()
        self.label_B0.setText(str(casoprueba1.B0))
        self.label_B1.setText(str(casoprueba1.B1))
        self.label_rxy.setText(str(casoprueba1.rxy))
        self.label_r2.setText(str(casoprueba1.r2))
        self.label_Yk.setText(str(casoprueba1.Yk))

    def botonPrueba2Click(self):
        casoprueba2 = CasoPrueba2()
        casoprueba2.leerDatos()
        casoprueba2.RealizarCalculo()
        self.label_B0.setText(str(casoprueba2.B0))
        self.label_B1.setText(str(casoprueba2.B1))
        self.label_rxy.setText(str(casoprueba2.rxy))
        self.label_r2.setText(str(casoprueba2.r2))
        self.label_Yk.setText(str(casoprueba2.Yk))

    def botonPrueba3Click(self):
        casoprueba3 = CasoPrueba3()
        casoprueba3.leerDatos()
        casoprueba3.RealizarCalculo()
        self.label_B0.setText(str(casoprueba3.B0))
        self.label_B1.setText(str(casoprueba3.B1))
        self.label_rxy.setText(str(casoprueba3.rxy))
        self.label_r2.setText(str(casoprueba3.r2))
        self.label_Yk.setText(str(casoprueba3.Yk))

    def botonPrueba4Click(self):        
        casoprueba4 = CasoPrueba4()
        casoprueba4.leerDatos()
        casoprueba4.RealizarCalculo()
        self.label_B0.setText(str(casoprueba4.B0))
        self.label_B1.setText(str(casoprueba4.B1))
        self.label_rxy.setText(str(casoprueba4.rxy))
        self.label_r2.setText(str(casoprueba4.r2))
        self.label_Yk.setText(str(casoprueba4.Yk))  
