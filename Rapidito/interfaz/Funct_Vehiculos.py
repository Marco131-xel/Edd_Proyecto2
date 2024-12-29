from PyQt6.QtCore import Qt
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
        self.ui.BT_buscar_most_vehi.clicked.connect(self.buscar_vehiculo_mostrar)
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
        archivo, _ = QFileDialog.getOpenFileName(self.ui.BT_abrir_vehiculos, "Seleccionar archivo Vehiculos", "",
                                                 "Archivos de texto (*.txt)")
        if archivo:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    for linea in f:
                        linea = linea.strip().strip(';')
                        datos = linea.split(':')
                        if len(datos) == 4:
                            placa = datos[0]
                            marca = datos[1]
                            modelo = int(datos[2])
                            precio = float(datos[3])

                            vehiculo = Vehiculos(placa, marca, modelo, precio)
                            self.arbol.insertar(vehiculo)
                            #self.ui.text_area.append(f'Cargado: {vehiculo}')
                            self.arbol.graficar("ArbolB")
                        else:
                            self.ui.ESTADOS.append(f'Linea invalida Vehiculos: {linea}')
                self.ui.ESTADOS.append('Carga completada Vehiculos')
            except Exception as e:
                self.ui.ESTADOS.append(f'Error al leer el archivo Vehiculos: {e}')

    # Funcion para crear un vehiculo
    def crear_vehiculo(self):
        try:
            int(self.ui.crear_MODELO.text())
            float(self.ui.crear_PRECIO.text())
        except ValueError:
            self.ui.estado_CREAR_vehiculo.setPlainText("Por favor ingresar datos validos")
            return
        placa = self.ui.crear_PLACA.text()
        marca = self.ui.crear_MARCA.text()
        modelo = self.ui.crear_MODELO.text()
        precio = self.ui.crear_PRECIO.text()

        # Crear Vehiculos
        vehiculo = Vehiculos(placa, marca, modelo, precio)
        self.arbol.insertar(vehiculo)
        self.limpiar_campos_crear()
        self.ui.estado_CREAR_vehiculo.append('Vehiculo agregado')
        self.arbol.graficar("ArbolB")

    # Funcion para buscar un vehiculo por su placa para modifcar
    def buscar_vehiculo_modificar(self):
        placa = self.ui.buscar_MOD_vehi.text().strip()
        vehiculo = self.arbol.buscar(placa)

        if vehiculo is not None:
            vehiculo_info = (
                f'Placa: {vehiculo.get_Placa()}, Marca: {vehiculo.get_Marca()}, Modelo: {vehiculo.get_Modelo()}, Precio: {vehiculo.get_Precio()}'
            )
            self.ui.estado_mod_vehiculo.setPlainText(vehiculo_info)
        else:
            # Si no se encuentra, mostrar error
            self.ui.estado_mod_vehiculo.setPlainText('No se encontro un vehiculo con la placa proporcionada')

    # Funcion para modicar los datos del vehiculo
    def modificar_vehiculo(self):
        placa = self.ui.buscar_MOD_vehi.text().strip()
        marca = self.ui.mod_MARCA.text().strip()
        modelo = self.ui.mod_MODELO.text().strip()
        precio = self.ui.mod_PRECIO.text().strip()

        if not placa:
            self.ui.estado_mod_vehiculo.setPlainText('Por favor ingrese la placa del vehículo a modificar')
            return

        if modelo and not modelo.isdigit():
            self.ui.estado_mod_vehiculo.setPlainText('El modelo debe ser un número entero')
            return

        if precio:
            try:
                precio = float(precio)
            except ValueError:
                self.ui.estado_mod_vehiculo.setPlainText('El precio debe ser un número válido')
                return

        # LLamar la funcion modificar vehiculo
        modificado = self.arbol.modificar(
            placa = placa,
            nueva_marca = marca if marca else None,
            nuevo_modelo = int(modelo) if modelo else None,
            nuevo_precio = precio if precio else None
        )
        if modificado:
            self.ui.mod_MARCA.clear()
            self.ui.mod_MODELO.clear()
            self.ui.mod_PRECIO.clear()
            self.ui.estado_mod_vehiculo.setPlainText('Vehiculo Modificado')
            self.arbol.graficar("ArbolB")
        else:
            self.ui.estado_mod_vehiculo.setPlainText('No se encontro el vehiculo')

    # Funcion para buscar el vehiculo y mostar
    def buscar_vehiculo_mostrar(self):
        placa = self.ui.buscar_MOST_vehi.text()
        vehiculo = self.arbol.buscar(placa)

        if vehiculo is not None:
            vehiculo_info = (
                'Datos del Vehiculo:\n'
                f'Placa: {vehiculo.get_Placa()}\n'
                f'Marca: {vehiculo.get_Marca()}\n'
                f' Modelo: {vehiculo.get_Modelo()}\n'
                f' Precio: {vehiculo.get_Precio()}\n'
            )
            self.ui.contenido_most_vehi.setPlainText(vehiculo_info)
        else:
            # Si no se encuentra, mostrar error
            self.ui.contenido_most_vehi.setPlainText('No se encontro un vehiculo con la placa proporcionada')

    # Funcion par eliminar vehiculo del arbol
    def eliminar_vehiculo(self):
        placa = self.ui.buscar_ELI_vehi.text().strip()

        # Verificar si el vehículo existe antes de eliminarlo
        vehiculo = self.arbol.buscar(placa)
        if vehiculo is not None:
            self.arbol.eliminar(placa)
            self.ui.estado_eli_vehi.setPlainText('Vehiculo eliminado')
            self.ui.contenido_eli_vehi.clear()
            self.ui.buscar_ELI_vehi.clear()
            self.arbol.graficar("ArbolB")
        else:
            self.ui.estado_eli_vehi.setPlainText('No se encontro un vehiculo. No se pudo eliminar')
            self.ui.contenido_eli_vehi.clear()

    # Funcion para buscar la placa a eliminar
    def buscar_eliminar(self):
        placa = self.ui.buscar_ELI_vehi.text().strip()
        vehiculo = self.arbol.buscar(placa)
        if vehiculo is not None:
            vehiculo_info = (
                'Datos del Vehiculo:\n'
                f'Placa: {vehiculo.get_Placa()}\n'
                f'Marca: {vehiculo.get_Marca()}\n'
                f' Modelo: {vehiculo.get_Modelo()}\n'
                f' Precio: {vehiculo.get_Precio()}\n'
            )
            self.ui.estado_eli_vehi.setPlainText('Vehiculo encontrado')
            self.ui.contenido_eli_vehi.setPlainText(vehiculo_info)
        else:
            # Si no se encuentra, mostrar error
            self.ui.estado_eli_vehi.setPlainText('Vehiculo no encontrado')
            self.ui.contenido_eli_vehi.setPlainText('No existe Datos del Vehiculo')

    # Funcion para limpiar los campos de crear vehiculo
    def limpiar_campos_crear(self):
        self.ui.crear_PLACA.clear()
        self.ui.crear_MARCA.clear()
        self.ui.crear_MODELO.clear()
        self.ui.crear_PRECIO.clear()
        self.ui.estado_CREAR_vehiculo.clear()
    # Funcion para limpiar los campos de modificar vehiculo
    def limpiar_campos_modificar(self):
        self.ui.buscar_MOD_vehi.clear()
        self.ui.estado_mod_vehiculo.clear()
        self.ui.mod_MARCA.clear()
        self.ui.mod_MODELO.clear()
        self.ui.mod_PRECIO.clear()
    # Funcion para limpiar el contenidod de mostrar vehiculos
    def limpiar_contenido_mostrar(self):
        self.ui.buscar_MOST_vehi.clear()
        self.ui.contenido_most_vehi.clear()
    # Funcion para graficar la estructura Arbol B
    def graficar_vehiculo(self):
        dialog = QDialog(parent=None)
        dialog.setWindowTitle('Grafica Estructura de Vehiculos')

        label = QLabel()
        pixmap = QPixmap("/home/marco/Documentos/Diciembre/edd/Edd_Proyecto2/Rapidito/ArbolB.png")
        label.setPixmap(pixmap)

        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        scroll_area = QScrollArea()
        scroll_area.setWidget(label)

        layout = QVBoxLayout(dialog)
        layout.addWidget(scroll_area)

        dialog.resize(1100, 400)

        dialog.exec()