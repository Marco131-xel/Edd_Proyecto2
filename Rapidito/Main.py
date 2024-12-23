import sys
from PyQt6.QtWidgets import *
from interfaz.Interfaz import Ui_MainWindow
from interfaz.Funct_Cliente import Funct_Cliente
from interfaz.Funct_Rutas import Funct_Rutas
from interfaz.Funct_Vehiculos import Funct_Vehiculos

#Iniciar mi interfaz
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Rapidito')

        # Intanciasr funcionalidades de la interfaz
        self.funct_cliente = Funct_Cliente(self.ui)
        self.funct_rutas = Funct_Rutas(self.ui)
        self.funct_vehiculos = Funct_Vehiculos(self.ui)
        # Bloquear edicio text_Area
        self.ui.text_area.setReadOnly(True)

#iniciar la aplicacion
def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()