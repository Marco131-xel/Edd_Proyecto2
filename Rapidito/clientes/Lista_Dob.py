from NodoLD import NodoLD
from clientes.Clientes import Clientes


class Lista_Dob:

    # Iniciar la lista doblemente enlazada
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    # Verificar si la lista esta vacia
    def vacia(self):
        return self.primero is None

    # Funcion para agregar un cliente a la lista
    def agregar_cliente(self, cliente):
        if not isinstance(cliente, Clientes):
            print('Error: El dato deber ser una instancia de la clase Clientes')
            return

        nuevo = NodoLD(cliente)
        if self.vacia():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        self.size += 1

    # Funcion para buscar un cliente en la lista por DPI
    def buscar_cliente(self, dpi):
        aux = self.primero
        while aux is not None:
            if aux.dato.get_Dpi() == dpi:
                return  aux
            aux = aux.siguiente
        return None

    # Funcion para modificar un cliente en la lista por DPI
    def modificar_cliente(self, dpi, nombre=None, apellido=None, genero=None, telefono=None, direccion=None):
        nodo = self.buscar_cliente(dpi)
        if nodo is None:
            print(f'No se encontro un cliente con DPI: {dpi}')
            return False

        cliente = nodo.dato
        if nombre is not None:
            cliente.set_Nombre(nombre)
        if apellido is not None:
            cliente.set_Apellido(apellido)
        if genero is not None:
            cliente.set_Genero(genero)
        if telefono is not None:
            cliente.set_Telefono(telefono)
        if direccion is not None:
            cliente.set_Direccion(direccion)
        print(f'Cliente modificado con DPI: {dpi}')
        return True

    # Funcion para eliminar un cliente por el dpi
    def eliminar_cliente(self, dpi):
        nodo = self.buscar_cliente(dpi)
        if nodo is None:
            print(f'No se encontro un cliente con DPI: {dpi}')
            return False

        if nodo == self.primero: # es el primero
            self.eliminar_inicio()
        elif nodo == self.ultimo: # es el ultimo
            self.eliminar_final()
        else: # esta en el medio
            nodo.anterior.siguiente = nodo.siguiente
            nodo.anterior.anterior = nodo.anterior
            self.size -= 1
        print(f'Cliente eliminado con DPI: {dpi}')
        return True

    # Funcion mostrar cliente por el dpi
    def mostrar_clientes(self, dpi):
        nodo = self.buscar_cliente(dpi)
        if nodo is None:
            print(f'No se encontro un cliente con DPI: {dpi}')
        else:
            print(nodo.dato)

    # Funcion eliminar un nodo del inicio
    def eliminar_inicio(self):
        if self.vacia():
            print('La lista es vacia')
            return
        if self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
        self.size -= 1

    # Funcion eliminar un nodo del final
    def eliminar_final(self):
        if self.vacia():
            print('La lista es vacia')
            return
        if self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
        self.size -= 1

    # Funcion recorrer mostrar todos los clientes
    def recorrer(self):
        aux = self.primero
        while aux is not None:
            print(aux.dato)
            aux = aux.siguiente
