from load.load_menu_principal import *
from PyQt5 import QtWidgets
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    ventana = MenuPrincipal()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
    