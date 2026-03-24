from PyQt5 import QtWidgets, uic, QtCore
from Integracion.Integracion import Integracion

class VentanaIntegracion(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_integracion_numerica.ui", self)
        self.show()

        self.botonCalcular.clicked.connect(self.botonCalcularClick)

    def botonCalcularClick(self):
        dof = int(self.lineEdit_dof.text())
        x = float(self.lineEdit_x.text())
        integracion = Integracion(x, dof)
        
        resultado = integracion.integrar(x, dof)
        self.label_resultado.setText(str(resultado))