from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from clientes.Clientes import Clientes
from clientes.Lista_Dob import Lista_Dob

class Funct_Cliente:
    def __init__(self, ui):
        self.ui = ui

        # Iniciar lista Doblemente Enlazada
        self.lista_clientes = Lista_Dob()
        # Conectar el boton para abrir Clientes
        self.ui.BT_abrir_clientes.clicked.connect(self.abrir_clientes)
        # Conectar boton para crear clientes
        self.ui.BT_crear_cliente.clicked.connect(self.crear_cliente)
        # Conectar boton buscar para modificar
        self.ui.BT_buscar_most.clicked.connect(self.buscar_cliente_mostrar)
        # Conectar boton para limpiar mostrar clientes
        self.ui.BT_limpiar_cliente.clicked.connect(self.limpiar_clientes)
        # Conectar boton para buscar modificar clientes
        self.ui.BT_buscar_mod.clicked.connect(self.buscar_cliente_modificar)
        # Conectar boton para modificar los clientes
        self.ui.BT_guardar_mod.clicked.connect(self.modificar_clientes)
        # Boton para limpiar lo de modificar clientes
        self.ui.BT_limpiar_mod_cliente.clicked.connect(self.limpiar_modificar)
        # Boton para buscar la eliminacion de clientes
        self.ui.BT_buscar_eli.clicked.connect(self.buscar_eliminar)
        self.ui.BT_eliminar.clicked.connect(self.eliminar_cliente)
        # Bloquear edicion a los estados
        self.ui.estado_crear.setReadOnly(True)
        self.ui.estado_mod.setReadOnly(True)
        self.ui.estado_eli.setReadOnly(True)
        self.ui.contenido_mostrar.setReadOnly(True)
        self.ui.contenido_eliminado.setReadOnly(True)
        # Funcion para graficar la estructura de los clientes
        self.ui.BT_graficar_cliente.clicked.connect(self.graficar_clientes)

    def abrir_clientes(self):
        # Abrir un cuadro de diálogo para seleccionar el archivo
        archivo, _ = QFileDialog.getOpenFileName(self.ui.BT_abrir_clientes, "Seleccionar archivo", "",
                                                 "Archivos de texto (*.txt)")
        if archivo:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    for linea in f:
                        linea = linea.strip().strip(';')
                        datos = linea.split(',')
                        if len(datos) == 6:
                            dpi = datos[0]
                            nombre = datos[1]
                            apellido = datos[2]
                            genero = datos[3]
                            telefono = datos[4]
                            direccion = datos[5]

                            cliente = Clientes(dpi, nombre, apellido, genero, telefono, direccion)
                            self.lista_clientes.agregar_cliente(cliente)
                            self.ui.text_area.append(f'Cargado: {cliente}')
                            self.lista_clientes.graficar("Lista_Dob")
                        else:
                            self.ui.text_area.append(f'Línea inválida: {linea}')
                self.ui.text_area.append('Carga completada')
            except Exception as e:
                self.ui.text_area.append(f'Error al leer el archivo: {e}')

    # Funcion para crear clientes en la interfaz
    def crear_cliente(self):
        try:
            dpi = int(self.ui.crear_DPI.text())
            #telefono = int(self.ui.crear_Telefono.text())
        except ValueError:
            self.ui.estado_crear.setPlainText("Por favor ingresar datos validos")
            return
        dpi = self.ui.crear_DPI.text()
        nombre = self.ui.crear_NOMBRE.text()
        apellido = self.ui.crear_APELLIDO.text()
        genero = self.ui.crear_GENERO.text()
        telefono = self.ui.crear_TELEFONO.text()
        direccion = self.ui.crear_DIRECCION.text()

        # crear los clientes
        cliente = Clientes(dpi, nombre, apellido, genero, telefono, direccion)
        self.lista_clientes.agregar_cliente(cliente)
        self.limpiar_campos()
        self.ui.estado_crear.append('Cliente Agregado')
        print(f'cliente creado: {cliente}')

    # Funcion para buscar los clientes a modificar
    def buscar_cliente_modificar(self):
        try:
            dpi = int(self.ui.buscar_dpi_MOD.text())
        except ValueError:
            self.ui.estado_mod.setPlainText("Por favor ingresar un DPI valido")
            return
        # Obtener dpí
        dpi = self.ui.buscar_dpi_MOD.text()
        nodo_cliente = self.lista_clientes.buscar_cliente(dpi)

        if nodo_cliente is not None:
            cliente = nodo_cliente.dato  # Obtener cliente del nodo
            # Formatear los datos del cliente para mostrarlos en el QTextEdit
            cliente_info = (
                f"DPI: {cliente.get_Dpi()}, Nombre: {cliente.get_Nombre()}, Apellido: {cliente.get_Apellido()}, Genero: {cliente.get_Genero()}, Telefono: {cliente.get_Telefono()}, Direccion: {cliente.get_Direccion()}"
            )
            self.ui.estado_mod.setPlainText(cliente_info)  # Mostrar los datos en el QTextEdit
            self.lista_clientes.mostrar_clientes(dpi)
        else:
            # Si no se encuentra, mostrar un mensaje de error
            self.ui.estado_mod.setPlainText("No se encontro un cliente con el DPI proporcionado")
    # Funcion para modificar los datos de los clientes
    def modificar_clientes(self):
        # Validar que el DPI es un numero válido
        dpi = self.ui.buscar_dpi_MOD.text().strip()
        if not dpi.isdigit():
            self.ui.estado_mod.setPlainText("Por favor ingresa DPI valido")
            return
        # Obtener datos
        nombre = self.ui.mod_NOMBRE.text().strip()
        apellido = self.ui.mod_APELLIDO.text().strip()
        genero = self.ui.mod_GENERO.text().strip()
        telefono = self.ui.mod_TELEFONO.text().strip()
        direccion = self.ui.mod_DIRECCION.text().strip()

        # Validar el telefono
        if telefono and not telefono.isdigit():
            self.ui.estado_mod.setPlainText("Por favor ingresa un numero de telefono valido")
            return

        # Llamar a la función modificar_cliente
        try:
            modificado = self.lista_clientes.modificar_cliente(
                dpi=dpi,
                nombre=nombre if nombre else None,
                apellido=apellido if apellido else None,
                genero=genero if genero else None,
                telefono=int(telefono) if telefono else None,
                direccion=direccion if direccion else None,
            )
            if modificado:
                self.ui.estado_mod.setPlainText("Cliente modificado")
            else:
                self.ui.estado_mod.setPlainText(f"No se encontro un cliente con el DPI: {dpi}")
        except Exception as e:
            self.ui.estado_mod.setPlainText(f"Error al modificar el cliente: {str(e)}")

    # Funcion para mostrar los clientes
    def buscar_cliente_mostrar(self):
        try:
            dpi = int(self.ui.buscar_dpi_MOST.text())
        except ValueError:
            self.ui.contenido_mostrar.setPlainText("Por favor ingresar un DPI valido")
            return
        # Obtener dpí
        dpi = self.ui.buscar_dpi_MOST.text()
        nodo_cliente = self.lista_clientes.buscar_cliente(dpi)

        if nodo_cliente is not None:
            cliente = nodo_cliente.dato  # Obtener cliente del nodo
            # Formatear los datos del cliente para mostrarlos en el QTextEdit
            cliente_info = (
                f"DPI: {cliente.get_Dpi()}\n"
                f"Nombre: {cliente.get_Nombre()}\n"
                f"Apellido: {cliente.get_Apellido()}\n"
                f"Genero: {cliente.get_Genero()}\n"
                f"Telefono: {cliente.get_Telefono()}\n"
                f"Direccion: {cliente.get_Direccion()}\n"
            )
            self.ui.contenido_mostrar.setPlainText(cliente_info)  # Mostrar los datos en el QTextEdit
            self.lista_clientes.mostrar_clientes(dpi)
        else:
            # Si no se encuentra, mostrar un mensaje de error
            self.ui.contenido_mostrar.setPlainText("No se encontro un cliente con el DPI proporcionado")

    # Buscar eliminacion del cliente
    def buscar_eliminar(self):
        try:
            dpi = int(self.ui.buscar_dpi_ELI.text())
        except ValueError:
            self.ui.estado_eli.setPlainText("Por favor ingresar un DPI valido")
            return
        # Obtener dpí
        dpi = self.ui.buscar_dpi_ELI.text()
        nodo_cliente = self.lista_clientes.buscar_cliente(dpi)

        if nodo_cliente is not None:
            cliente = nodo_cliente.dato  # Obtener cliente del nodo
            # Formatear los datos del cliente para mostrarlos en el QTextEdit
            cliente_info = (
                f"DPI: {cliente.get_Dpi()}, Nombre: {cliente.get_Nombre()}, Apellido: {cliente.get_Apellido()}, Genero: {cliente.get_Genero()}, Telefono: {cliente.get_Telefono()}, Direccion: {cliente.get_Direccion()}"
            )
            self.ui.estado_eli.setPlainText(cliente_info)  # Mostrar los datos en el QTextEdit
            self.lista_clientes.mostrar_clientes(dpi)
        else:
            # Si no se encuentra, mostrar un mensaje de error
            self.ui.estado_eli.setPlainText("No se encontro un cliente con el DPI proporcionado")
    # Eliminar un cliente
    def eliminar_cliente(self):
        # Validar que el DPI es un numero válido
        dpi = self.ui.buscar_dpi_ELI.text().strip()
        if not dpi.isdigit():
            self.ui.estado_eli.setPlainText("Por favor ingresa DPI valido")
            return
        # Obtener DPI
        nodo_cliente = self.lista_clientes.buscar_cliente(dpi)

        if nodo_cliente is not None:
            cliente = nodo_cliente.dato #Obtener cliente del nodo
            # Formatear los datos del cliente para mostrar en el estado
            cliente_info = (
                f"DPI: {cliente.get_Dpi()}\n"
                f"Nombre: {cliente.get_Nombre()}\n"
                f"Apellido: {cliente.get_Apellido()}\n"
                f"Genero: {cliente.get_Genero()}\n"
                f"Telefono: {cliente.get_Telefono()}\n"
                f"Direccion: {cliente.get_Direccion()}\n"
            )
            self.ui.contenido_eliminado.setPlainText(cliente_info)
            self.ui.estado_eli.setPlainText("Cliente eliminado")
            self.lista_clientes.mostrar_clientes(dpi)
            self.lista_clientes.eliminar_cliente(dpi)
        else:
            # si no se encuetra mostrar mensaje de error
            self.ui.estado_eli.setPlainText("No se encontro un cliente con el DPI proporcionado")

    # Limpiar campos de entrada
    def limpiar_campos(self):
        self.ui.crear_DPI.clear()
        self.ui.crear_NOMBRE.clear()
        self.ui.crear_APELLIDO.clear()
        self.ui.crear_GENERO.clear()
        self.ui.crear_TELEFONO.clear()
        self.ui.crear_DIRECCION.clear()

    # Limpiar contenido de clientes
    def limpiar_clientes(self):
        self.ui.contenido_mostrar.clear()
        self.ui.buscar_dpi_MOST.clear()

    # Limpiar contenido a modificar
    def limpiar_modificar(self):
        self.ui.estado_mod.clear()
        self.ui.buscar_dpi_MOD.clear()
        self.ui.mod_NOMBRE.clear()
        self.ui.mod_APELLIDO.clear()
        self.ui.mod_GENERO.clear()
        self.ui.mod_TELEFONO.clear()
        self.ui.mod_DIRECCION.clear()

    # Función para mostrar la estructura de graphviz
    def graficar_clientes(self):
        # Crear un QDialog sin un padre explícito
        dialog = QDialog(parent=None)
        dialog.setWindowTitle("Grafica Estrucutura de Clientes")

        # Crear un QLabel para mostrar la imagen
        label = QLabel(dialog)
        label.setPixmap(QPixmap("/home/marco/Documentos/Diciembre/edd/Edd_Proyecto2/Rapidito/Lista_Dob.png"))
        label.setScaledContents(True)

        # Configurar el tamaño del diálogo
        dialog.resize(1200, 600)
        dialog.exec()
