from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import os
from rutas.Grafo import Grafo
from rutas.Lista_Simp import Lista_Simp
from viajes.Viajes import Viajes
from viajes.Lista_Sviaje import Lista_Sviaje

class Funct_Viajes:
    def __init__(self, ui, lista_clientes, arbolito, lista_adyacencia):
        self.ui = ui

        # Inciar Estructuras
        self.lista_Dob = lista_clientes
        self.arbol = arbolito
        self.adyacencia = lista_adyacencia
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
        dpi = self.ui.MI_DPI.text()
        placa = self.ui.MI_PLACA.text()
        ruta = self.ui.comboRutaTomada.currentText()
        # Validar origen y destino
        if not origen or not destino:
            self.ui.SUPER_ESTADO.setPlainText('Selecciona origen y destino')
            return
        # Verificar si ya existe un viaje con el mismo id
        if self.lista_Sviaje.buscar_viaje(id):
            self.ui.SUPER_ESTADO.setPlainText('Error: Ya existe un viaje con este ID')
            return
        # Crear Nodos
        nodo_cliente = self.lista_Dob.buscar_cliente(dpi)
        if nodo_cliente is None:
            self.ui.SUPER_ESTADO.setPlainText('No se encontro DPI')
            return
        cliente = nodo_cliente.dato

        dato_cliente = {'DPI': cliente.get_Dpi(), 'Nombre': cliente.get_Nombre()}

        vehiculo = self.arbol.buscar(placa)
        # Verificar Ruta
        if not ruta:
            self.ui.SUPER_ESTADO.setPlainText('Selecciona una ruta')
            return
        if vehiculo is None:
            self.ui.SUPER_ESTADO.setPlainText('No se encontro Placa')
            return

        dato_vehiculo = {'Placa': vehiculo.get_Placa(),'Marca': vehiculo.get_Marca()}
        # Crear Viajes
        viajes = Viajes(id, origen, destino, fecha, dato_cliente, dato_vehiculo, ruta)
        self.lista_Sviaje.crear_viaje(viajes)
        self.limpiar_contenido()
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
        origen = self.ui.combo_ORIGEN.currentText()
        destino = self.ui.combo_DESTINO.currentText()

        # Obtener rutas desde el grafo
        grafo = Grafo(self.adyacencia.obtener_adyacencia())
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

        # Mostrar rutas en el comboBox
        self.ui.comboRutaTomada.clear()
        self.ui.SUPER_ESTADO.clear()
        self.ui.comboRutaTomada.addItem(f"Corta: {min_ruta[1]} segundos")
        self.ui.comboRutaTomada.addItem(f"Intermedia: {ruta_intermedia[1]} segundos")
        self.ui.comboRutaTomada.addItem(f"Larga: {max_ruta[1]} segundos")

        # Graficar las rutas
        self.graficar_ruta(min_ruta[0], "ruta_mas_corta")
        self.graficar_ruta(ruta_intermedia[0], "ruta_intermedia")
        self.graficar_ruta(max_ruta[0], "ruta_mas_larga")

        # Mostrar detalles de las rutas en consola
        print("Ruta mas corta:")
        for nodo in min_ruta[0]:
            print(nodo)
        print(f"Tiempo total: {min_ruta[1]}")

        print("\nRuta intermedia:")
        for nodo in ruta_intermedia[0]:
            print(nodo)
        print(f"Tiempo total: {ruta_intermedia[1]}")

        print("\nRuta mas larga:")
        for nodo in max_ruta[0]:
            print(nodo)
        print(f"Tiempo total: {max_ruta[1]}")
    # Funcion para limpiar los campos que se ingresaron
    def limpiar_contenido(self):
        self.ui.crear_ID.clear()
        self.ui.crear_FECHA.clear()
        self.ui.MI_DPI.clear()
        self.ui.MI_PLACA.clear()
        self.ui.espacio_DPI.clear()
        self.ui.espacio_PLACA.clear()
        self.ui.comboRutaTomada.clear()
    # Funcion para graficar la rutas movidas
    def graficar_ruta(self, ruta, filename):
        if not ruta:
            print("No hay ruta para graficar.")
            return

        dot = [
            "graph Ruta {",
            '  bgcolor="#17202a";',
            '  node [style=filled, fillcolor="#145a32", fontcolor="white", shape=circle, width=1.4, fixedsize=true];',
            '  edge [color="white", fontcolor="white"];',
        ]

        aux = ruta.primero
        while aux is not None and aux.siquiente is not None:
            origen = aux.ruta.get_Origen()
            destino = aux.siquiente.ruta.get_Origen()
            tiempo = aux.siquiente.ruta.get_Tiempo()

            # Asegurarse de que tiempo sea un numero y mayor que 0
            try:
                tiempo = int(tiempo)
                if destino and tiempo > 0:
                    dot.append(f'  "{origen}" -- "{destino}" [label="{tiempo} segundos"];')
                else:
                    print(f"Conexion invalida: origen={origen}, destino={destino}, tiempo={tiempo}")
            except ValueError:
                print(f"Valor no valido para tiempo: {tiempo} (origen={origen}, destino={destino})")
            aux = aux.siquiente

        dot.append("}")
        # Guardar archivo DOT
        dot_file = f"{filename}.dot"
        with open(dot_file, "w") as file:
            file.write("\n".join(dot))
        # Generar imagen PNG usando dot
        os.system(f"dot -Tpng {dot_file} -o {filename}.png")
        print(f"Grafico generado: {filename}.png")