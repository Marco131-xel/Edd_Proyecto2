import sys
from PyQt6.QtWidgets import *
from interfaz.Interfaz import Ui_MainWindow
from interfaz.Funct_Cliente import Funct_Cliente
from interfaz.Funct_Rutas import Funct_Rutas
from interfaz.Funct_Vehiculos import Funct_Vehiculos
from interfaz.Funct_Viajes import Funct_Viajes
from interfaz.Funct_Reportes import Funct_Reportes

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
        self.funct_viajes = Funct_Viajes(self.ui,self.funct_cliente.lista_clientes, self.funct_vehiculos.arbol,
                                         self.funct_rutas.lista_adyacencia)
        self.funct_reportes = Funct_Reportes(self.ui, self.funct_cliente.lista_clientes, self.funct_vehiculos.arbol,
                                             self.funct_rutas.lista_adyacencia, self.funct_viajes.lista_Sviaje)
        # Bloquear edicion
        self.ui.ESTADOS.setReadOnly(True)

#iniciar la aplicacion
def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()