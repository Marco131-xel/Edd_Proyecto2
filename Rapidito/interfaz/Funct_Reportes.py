from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
import os

class Funct_Reportes:
    def __init__(self, ui, clientes, vehiculos, rutas, viajes):
        self.ui = ui
        # Tener las listas de las demas clases
        self.lista_clientes = clientes
        self.lista_vehiculos = vehiculos
        self.lista_rutas = rutas
        self.lista_viajes = viajes

        self.ruta_actual = None
        # Iniciar los botones
        self.ui.BT_ver_topviajes.clicked.connect(self.top_Viajes)
        self.ui.BT_ver_topganancias.clicked.connect(self.top_Ganancias)
        self.ui.BT_ver_topclientes.clicked.connect(self.top_Clientes)
        self.ui.BT_ver_topvehiculos.clicked.connect(self.top_Vehiculos)
        self.ui.BT_buscar_rutaviaje.clicked.connect(self.buscar_rutaViaje)
        self.ui.graficar_rutaviaje.clicked.connect(self.mostrar_grafica)

        # Bloquear edicion
        self.ui.estado_topviajes.setReadOnly(True)
        self.ui.estado_topganancias.setReadOnly(True)
        self.ui.estado_topclientes.setReadOnly(True)
        self.ui.estado_topvehiculos.setReadOnly(True)
        self.ui.estado_rutaviaje.setReadOnly(True)
        self.ui.CONTENIDO_RUTAVIAJE.setReadOnly(True)

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
        datos_ganancias = []
        # iterar sobre la lista de viajes
        for viaje in self.lista_viajes:
            id = viaje.get_ID()
            origen = viaje.get_LugarOrigen()
            destino = viaje.get_LugarDestino()
            precio = viaje.get_Vehiculo().get_Precio()
            tiempo = viaje.get_Ruta_Tomada().get_Tiempo()
            total = tiempo * precio

            # agregar los datos
            datos_ganancias.append({
                'id': id,
                'origen': origen,
                'destino': destino,
                'tiempo': tiempo,
                'precio': precio,
                'total': total
            })
        # Ordenar por total en orden descendente
        datos_ganancias = sorted(datos_ganancias, key=lambda x: x['total'], reverse=True)[:5]

        # configurar la tabla
        self.ui.Table_ganancias.setRowCount(len(datos_ganancias))
        self.ui.Table_ganancias.setColumnCount(6)
        # Llenar la tabla con los datos
        for row, data in enumerate(datos_ganancias):
            self.ui.Table_ganancias.setItem(row, 0, QTableWidgetItem(str(data['id'])))
            self.ui.Table_ganancias.setItem(row, 1, QTableWidgetItem(data['origen']))
            self.ui.Table_ganancias.setItem(row, 2, QTableWidgetItem(data['destino']))
            self.ui.Table_ganancias.setItem(row, 3, QTableWidgetItem(str(data['tiempo'])))
            self.ui.Table_ganancias.setItem(row, 4, QTableWidgetItem(f"{data['precio']:.2f}"))
            self.ui.Table_ganancias.setItem(row, 5, QTableWidgetItem(f"{data['total']:.2f}"))
        # ajustar la tabla
        self.ui.Table_ganancias.resizeColumnsToContents()
        self.ui.estado_topganancias.setPlainText('Datos Encontrados')
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
        # Obtener ID del viaje
        id = self.ui.obtener_id.text().strip()
        viaje = self.lista_viajes.buscar_viaje(id)

        if viaje is None:
            self.ui.estado_rutaviaje.setPlainText('No se encontró el ID del viaje')
            self.ruta_actual = None
            return

        # Obtener los datos del cliente
        cliente_info = viaje.get_Cliente()
        dpi = cliente_info['DPI']
        nombre = cliente_info['Nombre']

        # Obtener los datos del vehículo
        vehiculo_info = viaje.get_Vehiculo()
        placa = vehiculo_info['Placa']
        marca = vehiculo_info['Marca']

        # Obtener los datos de origen y destino
        origen = viaje.get_LugarOrigen()
        destino = viaje.get_LugarDestino()

        # Mostrar los datos en la interfaz
        self.ui.CONTENIDO_RUTAVIAJE.setPlainText(
            f"ID: {viaje.get_ID()}\n"
            f"DPI: {dpi}\n"
            f"Nombre: {nombre}\n"
            f"Placa: {placa}\n"
            f"Marca: {marca}\n"
            f"Origen: {origen}\n"
            f"Destino: {destino}"
        )
        self.ui.estado_rutaviaje.clear()
        self.ui.estado_rutaviaje.setPlainText('ID Encontrado')
        # Guardar la ruta seleccionada
        self.ruta_actual = viaje.get_Ruta_Tomada()

    def mostrar_grafica(self):
        pass

    def graficar_rutaViaje(self, ruta, filename):
        if not ruta:
            print("No hay ruta para graficar.")
            return

        # Título del gráfico según el tipo de ruta tomada
        if "corta" in ruta:
            titulo = "Ruta Más Corta"
        elif "intermedia" in ruta:
            titulo = "Ruta Intermedia"
        elif "larga" in ruta:
            titulo = "Ruta Más Larga"
        else:
            titulo = "Ruta Desconocida"

        # Construir contenido del archivo DOT con orientación horizontal
        dot = [
            "graph Ruta {",
            f'  label="{titulo}";',
            '  labelloc="t";',
            '  fontsize=20;',
            '  fontcolor="white";',
            '  bgcolor="#17202a";',
            '  node [style=filled, fillcolor="#145a32", fontcolor="white", shape=circle, width=1.4, fixedsize=true];',
            '  edge [color="white", fontcolor="white"];',
            '  rankdir="LR";',  # Configurar para graficar de izquierda a derecha (horizontal)
        ]

        # Asumimos que la ruta es una lista de cadenas (lugares o destinos)
        for i in range(len(ruta) - 1):
            origen = ruta[i]
            destino = ruta[i + 1]
            tiempo = 10  # Si no tienes tiempo específico, puedes usar un valor predeterminado, o derivarlo de alguna otra manera

            # Agregar nodo actual al DOT
            dot.append(f'  "{origen}";')

            # Si hay un destino y no es el mismo nodo, añadir la conexión
            if destino and origen != destino:  # Evitar conexiones a sí mismos
                try:
                    dot.append(f'  "{origen}" -- "{destino}" [label="{tiempo} segundos"];')
                except ValueError:
                    print(f"Error al agregar la ruta entre {origen} y {destino}")

        # Cerrar el gráfico DOT
        dot.append("}")

        # Guardar el archivo DOT
        dot_file = f"{filename}.dot"
        with open(dot_file, "w") as file:
            file.write("\n".join(dot))

        # Generar la imagen PNG usando Graphviz
        result = os.system(f"dot -Tpng {dot_file} -o {filename}.png")
        if result == 0:
            print(f"Gráfico generado exitosamente: {filename}.png")
        else:
            print(f"Error al generar el gráfico: {filename}.png")
