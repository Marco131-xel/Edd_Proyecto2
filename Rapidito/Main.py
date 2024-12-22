import sys
from PyQt6.QtWidgets import *
from interfaz.Interfaz import Ui_MainWindow
from clientes.Clientes import Clientes
from clientes.Lista_Dob import Lista_Dob

# Probar mi arbol
from vehiculos.Vehiculos import Vehiculos
from vehiculos.ArbolB import ArbolB

# probar mi lista adyacencia
from rutas.Rutas import Ruta
from rutas.Lista_Ady import Lista_Ady

#Iniciar mi interfaz
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Rapidito')

        # iniciar mi lista doblemente enlazada
        self.lista_clientes = Lista_Dob()
        # iniciar mi arbol b
        self.arbol_vehiculos = ArbolB()
        # iniciar mi lista adyacencia
        self.lista_ady = Lista_Ady()
        # concectar el boton abrir clientes
        self.ui.BT_abrir_clientes.clicked.connect(self.abrir_clientes)
        # conectar el boton abrir vehiculos
        self.ui.BT_abrir_vehiculos.clicked.connect(self.abrir_vehiculos)
        # conectar el boton abrir rutas
        self.ui.BT_abrir_rutas.clicked.connect(self.abrir_rutas)

    def abrir_clientes(self):
        # Abriri un cuadro de dialogo para selccionar el archivo
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Archivos de texto (*.txt)")

        if archivo:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    for linea in f:
                        linea = linea.strip().strip(';')
                        # dividir los campos por linea
                        datos = linea.split(',')
                        if len(datos) == 6:
                            dpi = int(datos[0])
                            nombre = datos[1]
                            apellido = datos[2]
                            genero = datos[3]
                            telfono = int(datos[4])
                            direccion = datos[5]

                            cliente = Clientes(dpi, nombre, apellido, genero, telfono, direccion)
                            self.lista_clientes.agregar_cliente(cliente)
                            self.ui.text_area.append(f'Cargado: {cliente}')
                            self.lista_clientes.graficar("Lista_Dob")
                        else :
                            self.ui.text_area.append(f'Linea invalida: {linea}')
                self.ui.text_area.append(f'Carga comletada')
            except Exception as e:
                self.ui.text_area.append(f'Error al leear el archivo: {e}')

    # Funcion para abrir archivo de entrada vehiculos
    def abrir_vehiculos(self):
        # Abriri un cuadro
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Archivos de texto (*.txt)")

        if archivo:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    for linea in f:
                        linea = linea.strip().strip(';')
                        # dividir los campos por linea
                        datos = linea.split(':')
                        if len(datos) == 4:
                            placa = datos[0]
                            marca = datos[1]
                            modelo = int(datos[2])
                            precio = float(datos[3])

                            vehiculo = Vehiculos(placa, marca, modelo, precio)
                            self.arbol_vehiculos.insertar(vehiculo)
                            self.ui.text_area.append(f'Cargado: {vehiculo}')
                            self.arbol_vehiculos.graficar('ArbolB')
                        else :
                            self.ui.text_area.append(f'Linea invalida: {linea}')
                self.ui.text_area.append(f'Carga comletada')
            except Exception as e:
                self.ui.text_area.append(f'Error al leear el archivo: {e}')

    # Funcion abrir la rutas por archivo de entrada
    def abrir_rutas(self):
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Archivos de texto (*.txt)")
        if archivo:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    for linea in f:
                        linea = linea.strip().strip('%')
                        # dividir los campos por linea
                        datos = linea.split('/')
                        if len(datos) == 3:
                            origen = datos[0]
                            destino = datos[1]
                            tiempo = int(datos[2])

                            ruta = Ruta(origen, destino, tiempo)
                            self.lista_ady.agregar_ruta(ruta)
                            self.ui.text_area.append(f'Cargado: {ruta}')
                            self.lista_ady.graficar('Mapa')
                            self.lista_ady.mostrar_adyacencia()
                        else :
                            self.ui.text_area.append(f'Linea invalida: {linea}')
                self.ui.text_area.append(f'Carga comletada')
            except Exception as e:
                self.ui.text_area.append(f'Error al leear el archivo: {e}')


#iniciar la aplicacion
def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()