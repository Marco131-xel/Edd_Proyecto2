from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap

class Funct_Reportes:
    def __init__(self, ui, clientes, vehiculos, rutas, viajes):
        self.ui = ui
        # Tener las listas de las demas clases
        self.lista_clientes = clientes
        self.lista_vehiculos = vehiculos
        self.lista_rutas = rutas
        self.lista_viajes = viajes
        # Iniciar los botones
        self.ui.BT_ver_topviajes.clicked.connect(self.top_Viajes)
        self.ui.BT_ver_topganancias.clicked.connect(self.top_Ganancias)
        self.ui.BT_ver_topclientes.clicked.connect(self.top_Clientes)
        self.ui.BT_ver_topvehiculos.clicked.connect(self.top_Vehiculos)
        self.ui.BT_buscar_rutaviaje.clicked.connect(self.buscar_rutaViaje)
        self.ui.graficar_rutaviaje.clicked.connect(self.graficar_rutaViaje)

        # Bloquear edicion
        self.ui.estado_topviajes.setReadOnly(True)
        self.ui.estado_topganancias.setReadOnly(True)
        self.ui.estado_topclientes.setReadOnly(True)
        self.ui.estado_topvehiculos.setReadOnly(True)
        self.ui.estado_rutaviaje.setReadOnly(True)

    # Funcion para ver tabla top viajes
    def top_Viajes(self):
        #Table_Viajes
        viajes_ordenados = sorted(self.lista_viajes, key=lambda v: v.get_Ruta_Tomada(), reverse=True)
        top_viajes = viajes_ordenados[:5]
        # configurar la tabla
        if top_viajes:
            self.ui.Table_Viajes.setRowCount(len(top_viajes))
            self.ui.Table_Viajes.setColumnCount(4)

            # Rellenar la tabla
            for row, viaje in enumerate(top_viajes):
                self.ui.Table_Viajes.setItem(row, 0, QTableWidgetItem(str(viaje.get_ID())))
                self.ui.Table_Viajes.setItem(row, 1, QTableWidgetItem(viaje.get_LugarOrigen()))
                self.ui.Table_Viajes.setItem(row, 2, QTableWidgetItem(viaje.get_LugarDestino()))
                self.ui.Table_Viajes.setItem(row, 3, QTableWidgetItem(str(viaje.get_Ruta_Tomada())))
            # Ajustar las columnas al contenido
            self.ui.Table_Viajes.resizeColumnsToContents()
            self.ui.estado_topviajes.setPlainText('Datos Encotrados')
        else:
            self.ui.estado_topviajes.setPlainText('No hay Datos')

    def top_Ganancias(self):
        #Table_ganancias
        pass
    # Funcion para mostrar el top 5 de los clientes
    def top_Clientes(self):
        #Table_clientes
        conteo_viajes = {}
        #contar los viajes por cliente
        for viaje in self.lista_viajes:
            dpi = viaje.get_Cliente()['DPI']
            if dpi in conteo_viajes:
                conteo_viajes[dpi]['viajes'] += 1
            else:
                conteo_viajes[dpi] = {
                    'nombre' : viaje.get_Cliente()['Nombre'],
                    'viajes': 1
                }
        # Ordenar los clientes por numero de viajes
        clientes_top = sorted(conteo_viajes.items(), key=lambda item: item[1]['viajes'], reverse=True)[:5]
        # configurar la tabla
        if clientes_top:
            self.ui.Table_clientes.setRowCount(len(clientes_top))
            self.ui.Table_clientes.setColumnCount(3)
            # llenar la tabla con los datos del top 5
            for row, (dpi, data) in enumerate(clientes_top):
                self.ui.Table_clientes.setItem(row, 0, QTableWidgetItem(str(dpi)))
                self.ui.Table_clientes.setItem(row, 1, QTableWidgetItem(data['nombre']))
                self.ui.Table_clientes.setItem(row, 2, QTableWidgetItem(str(data['viajes'])))
            # ajustar las columnas al contenido
            self.ui.Table_clientes.resizeColumnsToContents()
            self.ui.estado_topclientes.setPlainText('Datos Encotrados')
        else:
            self.ui.estado_topclientes.setPlainText('No hay Datos')

    # Funcion para mostrar el top 5 de los vehiculos
    def top_Vehiculos(self):
        #Table_vehiculos
        conteo_viajes = {}
        # contar los viajes por vehiculo
        for viaje in self.lista_viajes:
            placa = viaje.get_Vehiculo()['Placa']
            if placa in conteo_viajes:
                conteo_viajes[placa]['viajes'] += 1
            else:
                conteo_viajes[placa] = {
                    'marca' : viaje.get_Vehiculo()['Marca'],
                    'viajes': 1
                }
        # ordenar los vehiculos por numero de viajes
        vehiculo_top = sorted(conteo_viajes.items(), key=lambda item: item[1]['viajes'], reverse=True)[:5]
        if vehiculo_top:
            # configurar la tabla
            self.ui.Table_vehiculos.setRowCount(len(vehiculo_top))
            self.ui.Table_vehiculos.setColumnCount(3)
            # LLenar la tabla con los datos del top 5
            for row, (placa, data) in enumerate(vehiculo_top):
                self.ui.Table_vehiculos.setItem(row, 0, QTableWidgetItem(str(placa)))
                self.ui.Table_vehiculos.setItem(row, 1, QTableWidgetItem(data['marca']))
                self.ui.Table_vehiculos.setItem(row, 2, QTableWidgetItem(str(data['viajes'])))
            # ajustar tabla
            self.ui.Table_vehiculos.resizeColumnsToContents()
            self.ui.estado_topvehiculos.setPlainText('Datos Encotrados')
        else:
            self.ui.estado_topvehiculos.setPlainText('No hay Datos')
    # Funcion para encontrar un viaje por el id
    def buscar_rutaViaje(self):
        #obtener_id
        id = self.ui.obtener_id.text().strip()
        viaje = self.lista_viajes.buscar_viaje(id)
    # Funcion para mostrar grafica por ruta viaje
    def graficar_rutaViaje(self):
        dialog = QDialog(parent=None)
        dialog.setWindowTitle('Grafica Ruta Viaje')

        label = QLabel()
        pixmap = QPixmap("/home/marco/Documentos/Diciembre/edd/Edd_Proyecto2/Rapidito/ArbolB.png")
        label.setPixmap(pixmap)

        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        scroll_area = QScrollArea()
        scroll_area.setWidget(label)

        layout = QVBoxLayout(dialog)
        layout.addWidget(scroll_area)

        dialog.resize(1200, 600)

        dialog.exec()