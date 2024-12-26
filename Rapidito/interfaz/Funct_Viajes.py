from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from clientes.Clientes import Clientes
from clientes.Lista_Dob import Lista_Dob
from vehiculos.Vehiculos import Vehiculos
from vehiculos.ArbolB import ArbolB
from rutas.Rutas import Ruta
from rutas.Lista_Simp import Lista_Simp
from viajes.Viajes import Viajes
from viajes.Lista_Sviaje import Lista_Sviaje

class Funct_Viajes:
    def __init__(self, ui, lista_clientes, arbolito):
        self.ui = ui

        # Inciar Estructuras
        self.lista_Dob = lista_clientes
        self.arbol = arbolito
        self.list_Simp = Lista_Simp()
        self.lista_Sviaje = Lista_Sviaje()
        # Iniciar Botones
        self.ui.BT_CREAR_viaje.clicked.connect(self.crear_viajes)
        self.ui.BT_buscar_DPI_viaje.clicked.connect(self.buscar_DPI)
        self.ui.BT_buscar_RUTA_viaje.clicked.connect(self.buscar_RUTA)
        self.ui.BT_buscar_PLACA_viaje.clicked.connect(self.buscar_PLACA)
        # Boton para limpiar los campos de viaje
        self.ui.BT_limpiar_viaje.clicked.connect(self.limpiar_contenido)
        # Boton para graficar la estructura lista simple
        self.ui.BT_graficar_viajes.clicked.connect(self.graficar_viajes)
        # Bloquear edicio a estados
        self.ui.espacio_DPI.setReadOnly(True)
        self.ui.espacio_PLACA.setReadOnly(True)
        self.ui.espacio_RUTA.setReadOnly(True)
        self.ui.SUPER_ESTADO.setReadOnly(True)


    # Funcion para crear viajes
    def crear_viajes(self):
        try:
            int(self.ui.crear_ID.text())
            int(self.ui.MI_DPI.text())
        except ValueError:
            self.ui.SUPER_ESTADO.setPlainText('PorFavor colocar numeros')
            return

        #  Obtener los datos
        id = self.ui.crear_ID.text()
        fecha = self.ui.crear_FECHA.text()
        origen = self.ui.combo_ORIGEN.currentText()
        destino = self.ui.combo_DESTINO.currentText()
        cliente = self.ui.MI_DPI.text()
        vehiculo = self.ui.MI_PLACA.text()
        ruta = self.ui.MI_RUTA.text()
        # Validar origen y destino
        if not origen or not destino:
            self.ui.SUPER_ESTADO.setPlainText('Selecciona origen y destino')
            return
        # Crear Viajes
        viajes = Viajes(id, origen, destino, fecha, cliente, vehiculo, ruta)
        self.lista_Sviaje.crear_viaje(viajes)
        self.ui.SUPER_ESTADO.setPlainText('Viaje Creado')
        self.lista_Sviaje.graficar('Lista_Viajes')
    # Funcion para graficar la estructura de viajes (Lista simple)
    def graficar_viajes(self):
        dialog = QDialog(parent=None)
        dialog.setWindowTitle('Grafica Estructura Viajes')

        label = QLabel()
        pixmap = QPixmap("/home/marco/Documentos/Diciembre/edd/Edd_Proyecto2/Rapidito/Lista_Viajes.png")
        label.setPixmap(pixmap)

        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        scroll = QScrollArea()
        scroll.setWidget(label)

        layout = QVBoxLayout(dialog)
        layout.addWidget(scroll)

        dialog.resize(1200, 600)
        dialog.exec()

    # Funcion para buscar el DPI
    def buscar_DPI(self):
        try:
            int(self.ui.MI_DPI.text())
        except ValueError:
            self.ui.SUPER_ESTADO.setPlainText('PorFavor colocar numeros')
            return
        dpi = self.ui.MI_DPI.text()
        nodo_cliente = self.lista_Dob.buscar_cliente(dpi)

        if nodo_cliente is not None:
            cliente = nodo_cliente.dato
            cliente_info = (
                f'DPI: {cliente.get_Dpi()}, Nombre: {cliente.get_Nombre()}'
            )
            self.ui.espacio_DPI.setPlainText(cliente_info)
        else:
            self.ui.espacio_DPI.setPlainText('No se encontro DPI')

    # Funcion para buscar la placa
    def buscar_PLACA(self):
        placa = self.ui.MI_PLACA.text()
        vehiculo = self.arbol.buscar(placa)

        if vehiculo is not None:
            vehiculo_info = (
                f'Placa: {vehiculo.get_Placa()}, Marca: {vehiculo.get_Marca()}'
            )
            self.ui.espacio_PLACA.setPlainText(vehiculo_info)
        else:
            self.ui.espacio_PLACA.setPlainText('No se encontro placa')

    # Funcion para buscar la ruta
    def buscar_RUTA(self):
        id = self.ui.crear_ID.text()
        self.lista_Sviaje.mostrar_viaje(id)
    # Funcion para limpiar los campos que se ingresaron
    def limpiar_contenido(self):
        self.ui.crear_ID.clear()
        self.ui.crear_FECHA.clear()
        self.ui.MI_DPI.clear()
        self.ui.MI_PLACA.clear()
        self.ui.MI_RUTA.clear()
        self.ui.espacio_DPI.clear()
        self.ui.espacio_PLACA.clear()
        self.ui.espacio_RUTA.clear()