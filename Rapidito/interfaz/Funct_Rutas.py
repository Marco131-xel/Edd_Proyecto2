from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QTextCursor, QPainter
from PyQt6.QtGui import QPixmap
from rutas.Rutas import Ruta
from rutas.Lista_Ady import Lista_Ady

class Funct_Rutas:
    def __init__(self, ui):
        self.ui = ui
        self.zoom_factor = 1.0
        # Iniciar lista adycencia
        self.lista_adyacencia = Lista_Ady()
        # Conectar el boton para abrir rutas
        self.ui.BT_abrir_rutas.clicked.connect(self.abrir_rutas)
        # Conectar el boton para el mapa
        self.ui.BT_mapa.clicked.connect(self.abrir_mapa)
        # Botones zoom
        self.ui.BT_zoom_mas.clicked.connect(self.zoom_in)
        self.ui.BT_zoom_menos.clicked.connect(self.zoom_out)

    # Funcion para cargar el archivo de entrada
    def abrir_rutas(self):
        # Abrir un cuadro de diálogo para seleccionar el archivo
        archivo, _ = QFileDialog.getOpenFileName(self.ui.BT_abrir_rutas, "Seleccionar archivo Rutas", "",
                                                 "Archivos de texto (*.txt)")
        if archivo:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    for linea in f:
                        linea = linea.strip().strip('%')
                        datos = linea.split('/')
                        if len(datos) == 3:
                            origen = datos[0]
                            destino = datos[1]
                            tiempo = datos[2]

                            ruta = Ruta(origen, destino, tiempo)
                            self.lista_adyacencia.agregar_ruta(ruta)
                            self.lista_adyacencia.graficar("Mapa")

                            # Crear comboBox
                            if origen not in [self.ui.combo_ORIGEN.itemText(i)
                                              for i in range(self.ui.combo_ORIGEN.count())]:
                                self.ui.combo_ORIGEN.addItem(origen)
                            if destino not in [self.ui.combo_DESTINO.itemText(i)
                                               for i in range(self.ui.combo_DESTINO.count())]:
                                self.ui.combo_DESTINO.addItem(destino)
                        else:
                            self.ui.ESTADOS.append(f'Linea invalida Rutas: {linea}')
                self.ui.ESTADOS.append('Carga completada Rutas')
            except Exception as e:
                self.ui.ESTADOS.append(f'Error al leer el archivo Rutas: {e}')

    # Funcion para abrir el mapa en la interfaz
    def abrir_mapa(self):
        ruta_imagen = "/home/marco/Documentos/Diciembre/edd/Edd_Proyecto2/Rapidito/Mapa.png"

        # Cargar imagen
        pixmap = QPixmap(ruta_imagen)
        if pixmap.isNull():
            self.ui.ESTADOS.append("Error: No se pudo cargar el mapa.")
            return

        self.scene = QGraphicsScene()
        self.scene.addPixmap(pixmap)

        self.ui.text_area.setScene(self.scene)
        self.ui.text_area.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.ui.text_area.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
        self.zoom_factor = 1.0
        self.ui.ESTADOS.append("Mapa cargado")

    def zoom_in(self):
        self.zoom_factor *= 1.2
        self.ui.text_area.scale(1.2, 1.2)

    def zoom_out(self):
        self.zoom_factor /= 1.2
        self.ui.text_area.scale(1 / 1.2, 1 / 1.2)
