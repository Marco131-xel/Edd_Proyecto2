# Form implementation generated from reading ui file 'Interfaz.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1348, 623)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BT_abrir_clientes = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_abrir_clientes.setGeometry(QtCore.QRect(10, 10, 111, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.BT_abrir_clientes.setFont(font)
        self.BT_abrir_clientes.setObjectName("BT_abrir_clientes")
        self.BT_abrir_vehiculos = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_abrir_vehiculos.setGeometry(QtCore.QRect(140, 10, 111, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.BT_abrir_vehiculos.setFont(font)
        self.BT_abrir_vehiculos.setObjectName("BT_abrir_vehiculos")
        self.BT_abrir_rutas = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_abrir_rutas.setGeometry(QtCore.QRect(260, 10, 111, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.BT_abrir_rutas.setFont(font)
        self.BT_abrir_rutas.setObjectName("BT_abrir_rutas")
        self.text_area = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.text_area.setGeometry(QtCore.QRect(20, 70, 811, 481))
        self.text_area.setStyleSheet("background-color: rgb(31, 31, 31);\n"
"color: rgb(170, 0, 255);")
        self.text_area.setObjectName("text_area")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(860, 70, 491, 481))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_cliente = QtWidgets.QWidget()
        self.tab_cliente.setObjectName("tab_cliente")
        self.tabWidget_2 = QtWidgets.QTabWidget(parent=self.tab_cliente)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 20, 451, 401))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_crear = QtWidgets.QWidget()
        self.tab_crear.setObjectName("tab_crear")
        self.crear_GENERO = QtWidgets.QLineEdit(parent=self.tab_crear)
        self.crear_GENERO.setGeometry(QtCore.QRect(310, 40, 113, 32))
        self.crear_GENERO.setObjectName("crear_GENERO")
        self.crear_TELEFONO = QtWidgets.QLineEdit(parent=self.tab_crear)
        self.crear_TELEFONO.setGeometry(QtCore.QRect(310, 100, 113, 32))
        self.crear_TELEFONO.setObjectName("crear_TELEFONO")
        self.crear_DIRECCION = QtWidgets.QLineEdit(parent=self.tab_crear)
        self.crear_DIRECCION.setGeometry(QtCore.QRect(90, 210, 331, 32))
        self.crear_DIRECCION.setObjectName("crear_DIRECCION")
        self.crear_DPI = QtWidgets.QLineEdit(parent=self.tab_crear)
        self.crear_DPI.setGeometry(QtCore.QRect(90, 20, 113, 32))
        self.crear_DPI.setObjectName("crear_DPI")
        self.crear_NOMBRE = QtWidgets.QLineEdit(parent=self.tab_crear)
        self.crear_NOMBRE.setGeometry(QtCore.QRect(90, 80, 131, 32))
        self.crear_NOMBRE.setObjectName("crear_NOMBRE")
        self.crear_APELLIDO = QtWidgets.QLineEdit(parent=self.tab_crear)
        self.crear_APELLIDO.setGeometry(QtCore.QRect(90, 150, 151, 32))
        self.crear_APELLIDO.setObjectName("crear_APELLIDO")
        self.BT_crear_cliente = QtWidgets.QPushButton(parent=self.tab_crear)
        self.BT_crear_cliente.setGeometry(QtCore.QRect(330, 300, 88, 34))
        self.BT_crear_cliente.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.BT_crear_cliente.setObjectName("BT_crear_cliente")
        self.label_2 = QtWidgets.QLabel(parent=self.tab_crear)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 31, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.tab_crear)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 58, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.tab_crear)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 58, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.tab_crear)
        self.label_5.setGeometry(QtCore.QRect(240, 40, 58, 18))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.tab_crear)
        self.label_6.setGeometry(QtCore.QRect(240, 100, 58, 18))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.tab_crear)
        self.label_7.setGeometry(QtCore.QRect(20, 220, 58, 18))
        self.label_7.setObjectName("label_7")
        self.estado_crear = QtWidgets.QTextEdit(parent=self.tab_crear)
        self.estado_crear.setGeometry(QtCore.QRect(30, 280, 171, 41))
        self.estado_crear.setObjectName("estado_crear")
        self.tabWidget_2.addTab(self.tab_crear, "")
        self.tab_modificar = QtWidgets.QWidget()
        self.tab_modificar.setObjectName("tab_modificar")
        self.buscar_dpi_MOD = QtWidgets.QLineEdit(parent=self.tab_modificar)
        self.buscar_dpi_MOD.setGeometry(QtCore.QRect(130, 10, 191, 32))
        self.buscar_dpi_MOD.setObjectName("buscar_dpi_MOD")
        self.label = QtWidgets.QLabel(parent=self.tab_modificar)
        self.label.setGeometry(QtCore.QRect(30, 20, 81, 18))
        self.label.setObjectName("label")
        self.estado_mod = QtWidgets.QTextEdit(parent=self.tab_modificar)
        self.estado_mod.setGeometry(QtCore.QRect(30, 60, 391, 61))
        self.estado_mod.setObjectName("estado_mod")
        self.mod_NOMBRE = QtWidgets.QLineEdit(parent=self.tab_modificar)
        self.mod_NOMBRE.setGeometry(QtCore.QRect(50, 150, 141, 32))
        self.mod_NOMBRE.setObjectName("mod_NOMBRE")
        self.mod_APELLIDO = QtWidgets.QLineEdit(parent=self.tab_modificar)
        self.mod_APELLIDO.setGeometry(QtCore.QRect(280, 150, 121, 32))
        self.mod_APELLIDO.setObjectName("mod_APELLIDO")
        self.mod_TELEFONO = QtWidgets.QLineEdit(parent=self.tab_modificar)
        self.mod_TELEFONO.setGeometry(QtCore.QRect(50, 210, 141, 32))
        self.mod_TELEFONO.setObjectName("mod_TELEFONO")
        self.mod_GENERO = QtWidgets.QLineEdit(parent=self.tab_modificar)
        self.mod_GENERO.setGeometry(QtCore.QRect(280, 210, 121, 32))
        self.mod_GENERO.setObjectName("mod_GENERO")
        self.mod_DIRECCION = QtWidgets.QLineEdit(parent=self.tab_modificar)
        self.mod_DIRECCION.setGeometry(QtCore.QRect(40, 280, 241, 32))
        self.mod_DIRECCION.setObjectName("mod_DIRECCION")
        self.BT_guardar_mod = QtWidgets.QPushButton(parent=self.tab_modificar)
        self.BT_guardar_mod.setGeometry(QtCore.QRect(320, 260, 88, 34))
        self.BT_guardar_mod.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.BT_guardar_mod.setObjectName("BT_guardar_mod")
        self.label_8 = QtWidgets.QLabel(parent=self.tab_modificar)
        self.label_8.setGeometry(QtCore.QRect(60, 130, 58, 18))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.tab_modificar)
        self.label_9.setGeometry(QtCore.QRect(290, 130, 58, 18))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.tab_modificar)
        self.label_10.setGeometry(QtCore.QRect(50, 190, 58, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.tab_modificar)
        self.label_11.setGeometry(QtCore.QRect(280, 190, 58, 18))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.tab_modificar)
        self.label_12.setGeometry(QtCore.QRect(50, 250, 71, 21))
        self.label_12.setObjectName("label_12")
        self.BT_buscar_mod = QtWidgets.QPushButton(parent=self.tab_modificar)
        self.BT_buscar_mod.setGeometry(QtCore.QRect(357, 10, 71, 34))
        self.BT_buscar_mod.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.BT_buscar_mod.setObjectName("BT_buscar_mod")
        self.BT_limpiar_mod_cliente = QtWidgets.QPushButton(parent=self.tab_modificar)
        self.BT_limpiar_mod_cliente.setGeometry(QtCore.QRect(320, 310, 88, 34))
        self.BT_limpiar_mod_cliente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.BT_limpiar_mod_cliente.setObjectName("BT_limpiar_mod_cliente")
        self.tabWidget_2.addTab(self.tab_modificar, "")
        self.tab_eliminar = QtWidgets.QWidget()
        self.tab_eliminar.setObjectName("tab_eliminar")
        self.label_13 = QtWidgets.QLabel(parent=self.tab_eliminar)
        self.label_13.setGeometry(QtCore.QRect(30, 30, 91, 18))
        self.label_13.setObjectName("label_13")
        self.BT_eliminar = QtWidgets.QPushButton(parent=self.tab_eliminar)
        self.BT_eliminar.setGeometry(QtCore.QRect(340, 320, 88, 34))
        self.BT_eliminar.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.BT_eliminar.setObjectName("BT_eliminar")
        self.buscar_dpi_ELI = QtWidgets.QLineEdit(parent=self.tab_eliminar)
        self.buscar_dpi_ELI.setGeometry(QtCore.QRect(130, 30, 201, 32))
        self.buscar_dpi_ELI.setObjectName("buscar_dpi_ELI")
        self.estado_eli = QtWidgets.QTextEdit(parent=self.tab_eliminar)
        self.estado_eli.setGeometry(QtCore.QRect(50, 80, 351, 41))
        self.estado_eli.setObjectName("estado_eli")
        self.contenido_eliminado = QtWidgets.QTextEdit(parent=self.tab_eliminar)
        self.contenido_eliminado.setGeometry(QtCore.QRect(50, 150, 351, 151))
        self.contenido_eliminado.setObjectName("contenido_eliminado")
        self.BT_buscar_eli = QtWidgets.QPushButton(parent=self.tab_eliminar)
        self.BT_buscar_eli.setGeometry(QtCore.QRect(347, 30, 81, 34))
        self.BT_buscar_eli.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.BT_buscar_eli.setObjectName("BT_buscar_eli")
        self.tabWidget_2.addTab(self.tab_eliminar, "")
        self.tab_mostrar = QtWidgets.QWidget()
        self.tab_mostrar.setObjectName("tab_mostrar")
        self.BT_buscar_most = QtWidgets.QPushButton(parent=self.tab_mostrar)
        self.BT_buscar_most.setGeometry(QtCore.QRect(350, 20, 71, 34))
        self.BT_buscar_most.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.BT_buscar_most.setObjectName("BT_buscar_most")
        self.buscar_dpi_MOST = QtWidgets.QLineEdit(parent=self.tab_mostrar)
        self.buscar_dpi_MOST.setGeometry(QtCore.QRect(140, 20, 191, 32))
        self.buscar_dpi_MOST.setObjectName("buscar_dpi_MOST")
        self.label_14 = QtWidgets.QLabel(parent=self.tab_mostrar)
        self.label_14.setGeometry(QtCore.QRect(30, 20, 91, 18))
        self.label_14.setObjectName("label_14")
        self.contenido_mostrar = QtWidgets.QTextEdit(parent=self.tab_mostrar)
        self.contenido_mostrar.setGeometry(QtCore.QRect(40, 100, 351, 171))
        self.contenido_mostrar.setObjectName("contenido_mostrar")
        self.BT_limpiar_cliente = QtWidgets.QPushButton(parent=self.tab_mostrar)
        self.BT_limpiar_cliente.setGeometry(QtCore.QRect(330, 300, 88, 34))
        self.BT_limpiar_cliente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.BT_limpiar_cliente.setObjectName("BT_limpiar_cliente")
        self.tabWidget_2.addTab(self.tab_mostrar, "")
        self.BT_graficar_cliente = QtWidgets.QPushButton(parent=self.tab_cliente)
        self.BT_graficar_cliente.setGeometry(QtCore.QRect(370, 10, 71, 31))
        self.BT_graficar_cliente.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.BT_graficar_cliente.setObjectName("BT_graficar_cliente")
        self.tabWidget.addTab(self.tab_cliente, "")
        self.tab_vehiculos = QtWidgets.QWidget()
        self.tab_vehiculos.setObjectName("tab_vehiculos")
        self.tabWidget_3 = QtWidgets.QTabWidget(parent=self.tab_vehiculos)
        self.tabWidget_3.setGeometry(QtCore.QRect(20, 20, 451, 401))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.crear_PLACA = QtWidgets.QLineEdit(parent=self.tab)
        self.crear_PLACA.setGeometry(QtCore.QRect(50, 60, 141, 32))
        self.crear_PLACA.setObjectName("crear_PLACA")
        self.crear_MARCA = QtWidgets.QLineEdit(parent=self.tab)
        self.crear_MARCA.setGeometry(QtCore.QRect(280, 60, 131, 32))
        self.crear_MARCA.setObjectName("crear_MARCA")
        self.crear_MODELO = QtWidgets.QLineEdit(parent=self.tab)
        self.crear_MODELO.setGeometry(QtCore.QRect(50, 150, 141, 32))
        self.crear_MODELO.setObjectName("crear_MODELO")
        self.crear_PRECIO = QtWidgets.QLineEdit(parent=self.tab)
        self.crear_PRECIO.setGeometry(QtCore.QRect(280, 150, 131, 32))
        self.crear_PRECIO.setObjectName("crear_PRECIO")
        self.label_15 = QtWidgets.QLabel(parent=self.tab)
        self.label_15.setGeometry(QtCore.QRect(60, 30, 58, 18))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.tab)
        self.label_16.setGeometry(QtCore.QRect(290, 30, 58, 18))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=self.tab)
        self.label_17.setGeometry(QtCore.QRect(60, 130, 58, 18))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.tab)
        self.label_18.setGeometry(QtCore.QRect(290, 130, 58, 18))
        self.label_18.setObjectName("label_18")
        self.estado_CREAR_vehiculo = QtWidgets.QTextEdit(parent=self.tab)
        self.estado_CREAR_vehiculo.setGeometry(QtCore.QRect(30, 260, 191, 41))
        self.estado_CREAR_vehiculo.setObjectName("estado_CREAR_vehiculo")
        self.BT_crear_vehiculos = QtWidgets.QPushButton(parent=self.tab)
        self.BT_crear_vehiculos.setGeometry(QtCore.QRect(290, 260, 88, 34))
        self.BT_crear_vehiculos.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.BT_crear_vehiculos.setObjectName("BT_crear_vehiculos")
        self.tabWidget_3.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.buscar_MOD_vehi = QtWidgets.QLineEdit(parent=self.tab_3)
        self.buscar_MOD_vehi.setGeometry(QtCore.QRect(120, 20, 181, 32))
        self.buscar_MOD_vehi.setObjectName("buscar_MOD_vehi")
        self.BT_buscar_mod_vehiculo = QtWidgets.QPushButton(parent=self.tab_3)
        self.BT_buscar_mod_vehiculo.setGeometry(QtCore.QRect(340, 20, 88, 34))
        self.BT_buscar_mod_vehiculo.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.BT_buscar_mod_vehiculo.setObjectName("BT_buscar_mod_vehiculo")
        self.BT_guardar_vehi = QtWidgets.QPushButton(parent=self.tab_3)
        self.BT_guardar_vehi.setGeometry(QtCore.QRect(330, 300, 88, 34))
        self.BT_guardar_vehi.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.BT_guardar_vehi.setObjectName("BT_guardar_vehi")
        self.BT_limpiar_mod_vehi = QtWidgets.QPushButton(parent=self.tab_3)
        self.BT_limpiar_mod_vehi.setGeometry(QtCore.QRect(330, 250, 88, 34))
        self.BT_limpiar_mod_vehi.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.BT_limpiar_mod_vehi.setObjectName("BT_limpiar_mod_vehi")
        self.label_19 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(20, 30, 91, 18))
        self.label_19.setObjectName("label_19")
        self.estado_mod_vehiculo = QtWidgets.QTextEdit(parent=self.tab_3)
        self.estado_mod_vehiculo.setGeometry(QtCore.QRect(30, 82, 381, 41))
        self.estado_mod_vehiculo.setObjectName("estado_mod_vehiculo")
        self.mod_MARCA = QtWidgets.QLineEdit(parent=self.tab_3)
        self.mod_MARCA.setGeometry(QtCore.QRect(50, 180, 141, 32))
        self.mod_MARCA.setObjectName("mod_MARCA")
        self.mod_MODELO = QtWidgets.QLineEdit(parent=self.tab_3)
        self.mod_MODELO.setGeometry(QtCore.QRect(280, 180, 141, 32))
        self.mod_MODELO.setObjectName("mod_MODELO")
        self.mod_PRECIO = QtWidgets.QLineEdit(parent=self.tab_3)
        self.mod_PRECIO.setGeometry(QtCore.QRect(50, 280, 151, 32))
        self.mod_PRECIO.setObjectName("mod_PRECIO")
        self.label_20 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(290, 150, 58, 18))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(60, 150, 58, 18))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(60, 250, 58, 18))
        self.label_22.setObjectName("label_22")
        self.tabWidget_3.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.buscar_ELI_vehi = QtWidgets.QLineEdit(parent=self.tab_2)
        self.buscar_ELI_vehi.setGeometry(QtCore.QRect(120, 30, 191, 32))
        self.buscar_ELI_vehi.setObjectName("buscar_ELI_vehi")
        self.estado_eli_vehi = QtWidgets.QTextEdit(parent=self.tab_2)
        self.estado_eli_vehi.setGeometry(QtCore.QRect(50, 80, 311, 41))
        self.estado_eli_vehi.setObjectName("estado_eli_vehi")
        self.label_23 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(20, 30, 91, 18))
        self.label_23.setObjectName("label_23")
        self.contenido_eli_vehi = QtWidgets.QTextEdit(parent=self.tab_2)
        self.contenido_eli_vehi.setGeometry(QtCore.QRect(40, 140, 321, 161))
        self.contenido_eli_vehi.setObjectName("contenido_eli_vehi")
        self.BT_eliminar_vehi = QtWidgets.QPushButton(parent=self.tab_2)
        self.BT_eliminar_vehi.setGeometry(QtCore.QRect(340, 320, 88, 34))
        self.BT_eliminar_vehi.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.BT_eliminar_vehi.setObjectName("BT_eliminar_vehi")
        self.BT_buscar_eli_vehi = QtWidgets.QPushButton(parent=self.tab_2)
        self.BT_buscar_eli_vehi.setGeometry(QtCore.QRect(340, 30, 88, 34))
        self.BT_buscar_eli_vehi.setObjectName("BT_buscar_eli_vehi")
        self.tabWidget_3.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_24 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_24.setGeometry(QtCore.QRect(20, 30, 91, 18))
        self.label_24.setObjectName("label_24")
        self.BT_buscar_most_vehi = QtWidgets.QPushButton(parent=self.tab_4)
        self.BT_buscar_most_vehi.setGeometry(QtCore.QRect(340, 20, 88, 34))
        self.BT_buscar_most_vehi.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.BT_buscar_most_vehi.setObjectName("BT_buscar_most_vehi")
        self.BT_limpiar_mos_vehi = QtWidgets.QPushButton(parent=self.tab_4)
        self.BT_limpiar_mos_vehi.setGeometry(QtCore.QRect(340, 320, 88, 34))
        self.BT_limpiar_mos_vehi.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.BT_limpiar_mos_vehi.setObjectName("BT_limpiar_mos_vehi")
        self.contenido_most_vehi = QtWidgets.QTextEdit(parent=self.tab_4)
        self.contenido_most_vehi.setGeometry(QtCore.QRect(40, 80, 361, 221))
        self.contenido_most_vehi.setObjectName("contenido_most_vehi")
        self.buscar_MOST_vehi = QtWidgets.QLineEdit(parent=self.tab_4)
        self.buscar_MOST_vehi.setGeometry(QtCore.QRect(120, 20, 191, 32))
        self.buscar_MOST_vehi.setObjectName("buscar_MOST_vehi")
        self.tabWidget_3.addTab(self.tab_4, "")
        self.BT_graficar_vehiculo = QtWidgets.QPushButton(parent=self.tab_vehiculos)
        self.BT_graficar_vehiculo.setGeometry(QtCore.QRect(377, 10, 71, 34))
        self.BT_graficar_vehiculo.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.BT_graficar_vehiculo.setObjectName("BT_graficar_vehiculo")
        self.tabWidget.addTab(self.tab_vehiculos, "")
        self.tab_viajes = QtWidgets.QWidget()
        self.tab_viajes.setObjectName("tab_viajes")
        self.label_25 = QtWidgets.QLabel(parent=self.tab_viajes)
        self.label_25.setGeometry(QtCore.QRect(70, 70, 51, 18))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(parent=self.tab_viajes)
        self.label_26.setGeometry(QtCore.QRect(270, 70, 58, 18))
        self.label_26.setObjectName("label_26")
        self.combo_ORIGEN = QtWidgets.QComboBox(parent=self.tab_viajes)
        self.combo_ORIGEN.setGeometry(QtCore.QRect(20, 100, 191, 32))
        self.combo_ORIGEN.setObjectName("combo_ORIGEN")
        self.label_27 = QtWidgets.QLabel(parent=self.tab_viajes)
        self.label_27.setGeometry(QtCore.QRect(20, 20, 41, 18))
        self.label_27.setObjectName("label_27")
        self.crear_ID = QtWidgets.QLineEdit(parent=self.tab_viajes)
        self.crear_ID.setGeometry(QtCore.QRect(60, 10, 61, 32))
        self.crear_ID.setObjectName("crear_ID")
        self.combo_DESTINO = QtWidgets.QComboBox(parent=self.tab_viajes)
        self.combo_DESTINO.setGeometry(QtCore.QRect(250, 100, 181, 32))
        self.combo_DESTINO.setObjectName("combo_DESTINO")
        self.BT_buscar_PLACA_viaje = QtWidgets.QPushButton(parent=self.tab_viajes)
        self.BT_buscar_PLACA_viaje.setGeometry(QtCore.QRect(410, 250, 61, 34))
        self.BT_buscar_PLACA_viaje.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.BT_buscar_PLACA_viaje.setObjectName("BT_buscar_PLACA_viaje")
        self.BT_buscar_DPI_viaje = QtWidgets.QPushButton(parent=self.tab_viajes)
        self.BT_buscar_DPI_viaje.setGeometry(QtCore.QRect(410, 180, 61, 34))
        self.BT_buscar_DPI_viaje.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.BT_buscar_DPI_viaje.setObjectName("BT_buscar_DPI_viaje")
        self.label_28 = QtWidgets.QLabel(parent=self.tab_viajes)
        self.label_28.setGeometry(QtCore.QRect(160, 20, 58, 18))
        self.label_28.setObjectName("label_28")
        self.crear_FECHA = QtWidgets.QLineEdit(parent=self.tab_viajes)
        self.crear_FECHA.setGeometry(QtCore.QRect(240, 10, 113, 32))
        self.crear_FECHA.setObjectName("crear_FECHA")
        self.MI_DPI = QtWidgets.QLineEdit(parent=self.tab_viajes)
        self.MI_DPI.setGeometry(QtCore.QRect(20, 180, 113, 32))
        self.MI_DPI.setObjectName("MI_DPI")
        self.MI_PLACA = QtWidgets.QLineEdit(parent=self.tab_viajes)
        self.MI_PLACA.setGeometry(QtCore.QRect(20, 260, 113, 32))
        self.MI_PLACA.setObjectName("MI_PLACA")
        self.label_29 = QtWidgets.QLabel(parent=self.tab_viajes)
        self.label_29.setGeometry(QtCore.QRect(70, 150, 31, 18))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(parent=self.tab_viajes)
        self.label_30.setGeometry(QtCore.QRect(60, 230, 41, 18))
        self.label_30.setObjectName("label_30")
        self.espacio_DPI = QtWidgets.QTextEdit(parent=self.tab_viajes)
        self.espacio_DPI.setGeometry(QtCore.QRect(160, 170, 231, 41))
        self.espacio_DPI.setObjectName("espacio_DPI")
        self.espacio_PLACA = QtWidgets.QTextEdit(parent=self.tab_viajes)
        self.espacio_PLACA.setGeometry(QtCore.QRect(160, 250, 231, 41))
        self.espacio_PLACA.setObjectName("espacio_PLACA")
        self.MI_RUTA = QtWidgets.QLineEdit(parent=self.tab_viajes)
        self.MI_RUTA.setGeometry(QtCore.QRect(20, 340, 113, 32))
        self.MI_RUTA.setObjectName("MI_RUTA")
        self.label_31 = QtWidgets.QLabel(parent=self.tab_viajes)
        self.label_31.setGeometry(QtCore.QRect(50, 310, 41, 18))
        self.label_31.setObjectName("label_31")
        self.BT_graficar_viajes = QtWidgets.QPushButton(parent=self.tab_viajes)
        self.BT_graficar_viajes.setGeometry(QtCore.QRect(390, 10, 88, 34))
        self.BT_graficar_viajes.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.BT_graficar_viajes.setObjectName("BT_graficar_viajes")
        self.espacio_RUTA = QtWidgets.QTextEdit(parent=self.tab_viajes)
        self.espacio_RUTA.setGeometry(QtCore.QRect(160, 330, 231, 41))
        self.espacio_RUTA.setObjectName("espacio_RUTA")
        self.BT_buscar_RUTA_viaje = QtWidgets.QPushButton(parent=self.tab_viajes)
        self.BT_buscar_RUTA_viaje.setGeometry(QtCore.QRect(410, 330, 61, 34))
        self.BT_buscar_RUTA_viaje.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.BT_buscar_RUTA_viaje.setObjectName("BT_buscar_RUTA_viaje")
        self.BT_CREAR_viaje = QtWidgets.QPushButton(parent=self.tab_viajes)
        self.BT_CREAR_viaje.setGeometry(QtCore.QRect(270, 390, 88, 34))
        self.BT_CREAR_viaje.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.BT_CREAR_viaje.setObjectName("BT_CREAR_viaje")
        self.BT_limpiar_viaje = QtWidgets.QPushButton(parent=self.tab_viajes)
        self.BT_limpiar_viaje.setGeometry(QtCore.QRect(380, 390, 88, 34))
        self.BT_limpiar_viaje.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.BT_limpiar_viaje.setObjectName("BT_limpiar_viaje")
        self.SUPER_ESTADO = QtWidgets.QTextEdit(parent=self.tab_viajes)
        self.SUPER_ESTADO.setGeometry(QtCore.QRect(20, 400, 221, 31))
        self.SUPER_ESTADO.setObjectName("SUPER_ESTADO")
        self.tabWidget.addTab(self.tab_viajes, "")
        self.tab_reportes = QtWidgets.QWidget()
        self.tab_reportes.setObjectName("tab_reportes")
        self.tabWidget.addTab(self.tab_reportes, "")
        self.BT_mapa = QtWidgets.QPushButton(parent=self.centralwidget)
        self.BT_mapa.setGeometry(QtCore.QRect(40, 570, 88, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.BT_mapa.setFont(font)
        self.BT_mapa.setObjectName("BT_mapa")
        self.ESTADOS = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.ESTADOS.setGeometry(QtCore.QRect(390, 10, 301, 41))
        self.ESTADOS.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.ESTADOS.setObjectName("ESTADOS")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BT_abrir_clientes.setText(_translate("MainWindow", "Abrir_Clientes"))
        self.BT_abrir_vehiculos.setText(_translate("MainWindow", "Abrir_Vehiculos"))
        self.BT_abrir_rutas.setText(_translate("MainWindow", "Abrir_Rutas"))
        self.BT_crear_cliente.setText(_translate("MainWindow", "Crear"))
        self.label_2.setText(_translate("MainWindow", "DPI"))
        self.label_3.setText(_translate("MainWindow", "Nombre"))
        self.label_4.setText(_translate("MainWindow", "Apellido"))
        self.label_5.setText(_translate("MainWindow", "Genero"))
        self.label_6.setText(_translate("MainWindow", "Telefono"))
        self.label_7.setText(_translate("MainWindow", "Direccion"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_crear), _translate("MainWindow", "Crear"))
        self.label.setText(_translate("MainWindow", "Buscar DPI"))
        self.BT_guardar_mod.setText(_translate("MainWindow", "Guardar"))
        self.label_8.setText(_translate("MainWindow", "Nombre"))
        self.label_9.setText(_translate("MainWindow", "Apellido"))
        self.label_10.setText(_translate("MainWindow", "Telefono"))
        self.label_11.setText(_translate("MainWindow", "Genero"))
        self.label_12.setText(_translate("MainWindow", "Direccion"))
        self.BT_buscar_mod.setText(_translate("MainWindow", "Buscar"))
        self.BT_limpiar_mod_cliente.setText(_translate("MainWindow", "Limpiar"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_modificar), _translate("MainWindow", "Modificar"))
        self.label_13.setText(_translate("MainWindow", "Buscar DPI"))
        self.BT_eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.BT_buscar_eli.setText(_translate("MainWindow", "Buscar"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_eliminar), _translate("MainWindow", "Eliminar"))
        self.BT_buscar_most.setText(_translate("MainWindow", "Buscar"))
        self.label_14.setText(_translate("MainWindow", "Buscar DPI"))
        self.BT_limpiar_cliente.setText(_translate("MainWindow", "Limpiar"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_mostrar), _translate("MainWindow", "Mostrar"))
        self.BT_graficar_cliente.setText(_translate("MainWindow", "Graficar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cliente), _translate("MainWindow", "Clientes"))
        self.label_15.setText(_translate("MainWindow", "Placa"))
        self.label_16.setText(_translate("MainWindow", "Marca"))
        self.label_17.setText(_translate("MainWindow", "Modelo"))
        self.label_18.setText(_translate("MainWindow", "Precio"))
        self.BT_crear_vehiculos.setText(_translate("MainWindow", "Crear"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab), _translate("MainWindow", "Crear"))
        self.BT_buscar_mod_vehiculo.setText(_translate("MainWindow", "Buscar"))
        self.BT_guardar_vehi.setText(_translate("MainWindow", "Guardar"))
        self.BT_limpiar_mod_vehi.setText(_translate("MainWindow", "Limpiar"))
        self.label_19.setText(_translate("MainWindow", "Buscar Placa"))
        self.label_20.setText(_translate("MainWindow", "Modelo"))
        self.label_21.setText(_translate("MainWindow", "Marca"))
        self.label_22.setText(_translate("MainWindow", "Precio"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), _translate("MainWindow", "Modificar"))
        self.label_23.setText(_translate("MainWindow", "Buscar Placa"))
        self.BT_eliminar_vehi.setText(_translate("MainWindow", "Eliminar"))
        self.BT_buscar_eli_vehi.setText(_translate("MainWindow", "Buscar"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_2), _translate("MainWindow", "Eliminar"))
        self.label_24.setText(_translate("MainWindow", "Buscar Placa"))
        self.BT_buscar_most_vehi.setText(_translate("MainWindow", "Buscar"))
        self.BT_limpiar_mos_vehi.setText(_translate("MainWindow", "Limpiar"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), _translate("MainWindow", "Mostrar"))
        self.BT_graficar_vehiculo.setText(_translate("MainWindow", "Graficar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_vehiculos), _translate("MainWindow", "Vehiculos"))
        self.label_25.setText(_translate("MainWindow", "Origen"))
        self.label_26.setText(_translate("MainWindow", "Destino"))
        self.label_27.setText(_translate("MainWindow", "ID"))
        self.BT_buscar_PLACA_viaje.setText(_translate("MainWindow", "Buscar"))
        self.BT_buscar_DPI_viaje.setText(_translate("MainWindow", "Buscar"))
        self.label_28.setText(_translate("MainWindow", "Fecha"))
        self.label_29.setText(_translate("MainWindow", "DPI"))
        self.label_30.setText(_translate("MainWindow", "Placa"))
        self.label_31.setText(_translate("MainWindow", "Ruta"))
        self.BT_graficar_viajes.setText(_translate("MainWindow", "Graficar"))
        self.BT_buscar_RUTA_viaje.setText(_translate("MainWindow", "Buscar"))
        self.BT_CREAR_viaje.setText(_translate("MainWindow", "Crear"))
        self.BT_limpiar_viaje.setText(_translate("MainWindow", "Limpiar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_viajes), _translate("MainWindow", "Viajes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_reportes), _translate("MainWindow", "Reportes"))
        self.BT_mapa.setText(_translate("MainWindow", "Mapa"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
