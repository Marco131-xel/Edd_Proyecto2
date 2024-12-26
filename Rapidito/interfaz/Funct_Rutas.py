from PyQt6.QtWidgets import *
from PyQt6.QtGui import QTextCursor
from rutas.Rutas import Ruta
from rutas.Lista_Ady import Lista_Ady

class Funct_Rutas:
    def __init__(self, ui):
        self.ui = ui

        # Iniciar lista adycencia
        self.lista_adyacencia = Lista_Ady()
        # Conectar el boton para abrir rutas
        self.ui.BT_abrir_rutas.clicked.connect(self.abrir_rutas)
        # Conectar el boton para el mapa
        self.ui.BT_mapa.clicked.connect(self.abrir_mapa)

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
        # Crear HTML para insertar la imagen
        html = f"""
                <html>
                    <body>
                        <img src="file://{ruta_imagen}" alt="Mapa" style="width: 100%; height: auto;">
                    </body>
                </html>
                """
        # Establecer el contenido en text_area
        self.ui.text_area.setHtml(html)
        cursor = self.ui.text_area.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.ui.text_area.setTextCursor(cursor)
