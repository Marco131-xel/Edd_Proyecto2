from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from vehiculos.Vehiculos import Vehiculos
from vehiculos.ArbolB import ArbolB

class Funct_Vehiculos:
    def __init__(self,ui):
        self.ui = ui
        # Inicar Arbol B
        self.arbol = ArbolB()
        # Inciar los botones
        self.ui.BT_abrir_vehiculos.clicked.connect(self.abrir_vehiculos)
        self.ui.BT_crear_vehiculos.clicked.connect(self.crear_vehiculo)
        self.ui.BT_buscar_mod_vehiculo.clicked.connect(self.buscar_vehiculo_modificar)
        self.ui.BT_guardar_vehi.clicked.connect(self.modificar_vehiculo)
        self.ui.BT_buscar_eli_vehi.clicked.connect(self.buscar_eliminar)
        self.ui.BT_eliminar_vehi.clicked.connect(self.eliminar_vehiculo)
        self.ui.buscar_MOST_vehi.clicked.connect(self.buscar_vehiculo_mostrar)
        # Botones para limpiar campos
        self.ui.BT_limpiar_mod_vehi.clicked.connect(self.limpiar_campos_modificar)
        self.ui.BT_limpiar_mos_vehi.clicked.connect(self.limpiar_contenido_mostrar)
        # Bloquear edicion de estados
        self.ui.contenido_most_vehi.setReadOnly(True)
        self.ui.contenido_eli_vehi.setReadOnly(True)
        self.ui.estado_eli_vehi.setReadOnly(True)
        self.ui.estado_mod_vehiculo.setReadOnly(True)
        self.ui.estado_CREAR_vehiculo.setReadOnly(True)

        # Boton para graficar la estructura del arbol
        self.ui.BT_graficar_vehiculo.clicked.connect(self.graficar_vehiculo)

    # Funcion para abrir el archivo de entrada vehiculos
    def abrir_vehiculos(self):
        pass
    # Funcion para crear un vehiculo
    def crear_vehiculo(self):
        pass
    # Funcion para buscar un vehiculo por su placa para modifcar
    def buscar_vehiculo_modificar(self):
        pass
    # Funcion para modicar los datos del vehiculo
    def modificar_vehiculo(self):
        pass
    # Funcion para buscar el vehiculo y mostar
    def buscar_vehiculo_mostrar(self):
        pass
    # Funcion par eliminar vehiculo del arbol
    def eliminar_vehiculo(self):
        pass
    # Funcion para buscar la placa a eliminar
    def buscar_eliminar(self):
        pass
    # Funcion para limpiar los campos de crear vehiculo
    def limpiar_campos_crear(self):
        pass
    # Funcion para limpiar los campos de modificar vehiculo
    def limpiar_campos_modificar(self):
        pass
    # Funcion para limpiar el contenidod de mostrar vehiculos
    def limpiar_contenido_mostrar(self):
        pass
    # Funcion para graficar la estructura Arbol B
    def graficar_vehiculo(self):
        pass