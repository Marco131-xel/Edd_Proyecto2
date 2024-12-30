from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
import os
from rutas.Grafo import Grafo

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
        # Lista para almacenar datos de los viajes
        datos_viajes = []

        # Iterar sobre la lista de viajes
        for viaje in self.lista_viajes:
            id = viaje.get_ID()
            origen = viaje.get_LugarOrigen()
            destino = viaje.get_LugarDestino()
            ruta_tomada = viaje.get_Ruta_Tomada()
            tiempo = int(ruta_tomada.split(":")[1].split()[0])
            datos_viajes.append({
                'id': id,
                'origen': origen,
                'destino': destino,
                'tiempo': tiempo
            })
        # Ordenar por tiempo en orden descendente
        datos_viajes = sorted(datos_viajes, key=lambda x: x['tiempo'], reverse=True)[:5]

        if datos_viajes:
            # Configurar la tabla
            self.ui.Table_Viajes.setRowCount(len(datos_viajes))
            self.ui.Table_Viajes.setColumnCount(4)
            # Rellenar la tabla con los datos
            for row, data in enumerate(datos_viajes):
                self.ui.Table_Viajes.setItem(row, 0, QTableWidgetItem(str(data['id'])))
                self.ui.Table_Viajes.setItem(row, 1, QTableWidgetItem(data['origen']))
                self.ui.Table_Viajes.setItem(row, 2, QTableWidgetItem(data['destino']))
                self.ui.Table_Viajes.setItem(row, 3, QTableWidgetItem(str(data['tiempo'])))

            # Ajustar las columnas al contenido
            self.ui.Table_Viajes.resizeColumnsToContents()
            self.ui.estado_topviajes.setPlainText('Datos Encontrados')
        else:
            self.ui.estado_topviajes.setPlainText('No hay Datos')

    # Funcion para mostrar el top 5 de los viajes mas caros
    def top_Ganancias(self):
        # Table_ganancias
        datos_ganancias = []

        # Iterar sobre la lista de viajes
        for viaje in self.lista_viajes:
            id = viaje.get_ID()
            origen = viaje.get_LugarOrigen()
            destino = viaje.get_LugarDestino()
            vehiculo = viaje.get_Vehiculo()
            if isinstance(vehiculo, dict):
                precio = vehiculo.get('Precio', 0)
            else:
                precio = vehiculo.get_Precio()
            precio = float(precio)
            ruta_tomada = viaje.get_Ruta_Tomada()
            tiempo = int(ruta_tomada.split(":")[1].split()[0])
            total = float(tiempo * precio)

            # Agregar los datos
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

        if datos_ganancias:
            # Configurar la tabla
            self.ui.Table_ganancias.setRowCount(len(datos_ganancias))
            self.ui.Table_ganancias.setColumnCount(6)

            # Llenar la tabla con los datos
            for row, data in enumerate(datos_ganancias):
                self.ui.Table_ganancias.setItem(row, 0, QTableWidgetItem(str(data['id'])))
                self.ui.Table_ganancias.setItem(row, 1, QTableWidgetItem(data['origen']))
                self.ui.Table_ganancias.setItem(row, 2, QTableWidgetItem(data['destino']))
                self.ui.Table_ganancias.setItem(row, 3, QTableWidgetItem(str(data['tiempo'])))
                self.ui.Table_ganancias.setItem(row, 4, QTableWidgetItem(
                    f"{data['precio']:.2f}"))
                self.ui.Table_ganancias.setItem(row, 5, QTableWidgetItem(f"{data['total']:.2f}"))

            # Ajustar la tabla
            self.ui.Table_ganancias.resizeColumnsToContents()
            self.ui.estado_topganancias.setPlainText('Datos Encontrados')
        else:
            self.ui.estado_topganancias.setPlainText('No hay Datos')
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
            f"Destino: {destino}\n"
            f"Ruta: {viaje.get_Ruta_Tomada()}\n"
        )
        self.ui.estado_rutaviaje.clear()
        self.ui.estado_rutaviaje.setPlainText('ID Encontrado')
        # Crear grafica
        grafo = Grafo(self.lista_rutas.obtener_adyacencia())
        rutas = grafo.encontrar_rutas(origen, destino)

        # Verificar si no existen rutas
        if not rutas:
            self.ui.SUPER_ESTADO.setPlainText('No existe una ruta seleccionada')
            return
        # Calcular tiempos para las rutas encontradas
        tiempos = grafo.calcular_tiempos(rutas)
        min_ruta, max_ruta = grafo.obtener_ruta_min_max(tiempos)
        # Calcular el tiempo promedio
        tiempos_totales = [tiempo[1] for tiempo in tiempos]
        promedio_tiempo = sum(tiempos_totales) / len(tiempos_totales)
        # Encontrar la ruta intermedia
        ruta_intermedia = min(tiempos, key=lambda x: abs(x[1] - promedio_tiempo))
        # Determinar cuál ruta fue tomada (corta, intermedia o larga)
        ruta_tomada = viaje.get_Ruta_Tomada()
        ruta_tomada_palabra = ruta_tomada.split(":")[0].strip()
        self.seleccion = ruta_tomada_palabra
        # Determinar eleccino
        if ruta_tomada_palabra == "Corta":
            self.graficar_ruta(min_ruta[0], "id_corta")
        elif ruta_tomada_palabra == "Intermedia":
            self.graficar_ruta(ruta_intermedia[0], "id_intermedia")
        elif ruta_tomada_palabra == "Larga":
            self.graficar_ruta(max_ruta[0], "id_larga")
        else:
            self.ui.SUPER_ESTADO.setPlainText('Ruta tomada desconocida')

    # Funcion mostar grafica id
    def mostrar_grafica(self):
        if not hasattr(self, 'seleccion') or not self.seleccion:
            self.ui.SUPER_ESTADO.setPlainText("Selecciona una ruta valida")
            return
        if "Corta" in self.seleccion:
            archivo = "id_corta.png"
        elif "Intermedia" in self.seleccion:
            archivo = "id_intermedia.png"
        elif "Larga" in self.seleccion:
            archivo = "id_larga.png"
        else:
            self.ui.SUPER_ESTADO.setPlainText("Ruta seleccionada no valida")
            return
        # Mostrar la imagen seleccionada en un diálogo
        dialog = QDialog(parent=None)
        dialog.setWindowTitle('Grafica de Ruta Viaje')
        label = QLabel()
        pixmap = QPixmap(archivo)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        scroll = QScrollArea()
        scroll.setWidget(label)
        layout = QVBoxLayout(dialog)
        layout.addWidget(scroll)
        dialog.resize(1100, 400)
        dialog.exec()
    # Función para graficar la ruta del viaje
    def graficar_ruta(self, ruta, filename):
        if not ruta:
            print("No hay ruta para graficar")
            return
        # Titulo
        if "corta" in filename:
            titulo = "Ruta mas Corta"
        elif "intermedia" in filename:
            titulo = "Ruta Intermedia"
        elif "larga" in filename:
            titulo = "Ruta mas Larga"
        else:
            titulo = "Ruta Desconocida"
        # Construir dot
        dot = [
            "graph Ruta {",
            f'  label="{titulo}";',
            '  labelloc="t";',
            '  fontsize=20;',
            '  fontcolor="white";',
            '  bgcolor="#17202a";',
            '  node [style=filled, fillcolor="#145a32", fontcolor="white", shape=circle, width=1.4, fixedsize=true];',
            '  edge [color="white", fontcolor="white"];',
            '  rankdir="LR";',
        ]

        # Recorrer la lista
        aux = ruta.primero
        while aux is not None:
            origen = aux.ruta.get_Origen()
            destino = aux.siquiente.ruta.get_Origen() if aux.siquiente else None
            tiempo = aux.ruta.get_Tiempo()
            # Agregar nodo actual al DOT
            dot.append(f'  "{origen}";')
            # Si hay un destino y no es el mismo nodo
            if destino and origen != destino:
                try:
                    tiempo = int(tiempo)
                    if tiempo > 0:
                        dot.append(f'  "{origen}" -- "{destino}" [label="{tiempo} segundos"];')
                except ValueError:
                    print(f"Tiempo no valido: {tiempo} (origen={origen}, destino={destino})")
            aux = aux.siquiente
        dot.append("}")
        # Guardar el archivo DOT
        dot_file = f"{filename}.dot"
        with open(dot_file, "w") as file:
            file.write("\n".join(dot))
        # Generar la imagen PNG usando Graphviz
        result = os.system(f"dot -Tpng {dot_file} -o {filename}.png")
        if result == 0:
            print(f"Grafico generado exitosamente: {filename}.png")
        else:
            print(f"Error al generar el grafico: {filename}.png")