from clientes.NodoLD import NodoLD
from clientes.Clientes import Clientes
import os


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
            print('Error: El dato debe ser una instancia de la clase Clientes')
            return

        nuevo = NodoLD(cliente)
        if self.vacia():
            self.primero = self.ultimo = nuevo
            self.primero.siguiente = self.primero.anterior = self.primero
        else:
            nuevo.anterior = self.ultimo
            nuevo.siguiente = self.primero
            self.ultimo.siguiente = nuevo
            self.primero.anterior = nuevo
            self.ultimo = nuevo
        self.size += 1

    # Funcion para buscar un cliente en la lista por DPI
    def buscar_cliente(self, dpi):
        if self.vacia():
            return None

        aux = self.primero
        while True:
            if aux.dato.get_Dpi() == dpi:
                return aux
            aux = aux.siguiente
            if aux == self.primero:
                break
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

        if nodo == self.primero and nodo == self.ultimo:  # unico nodo
            self.primero = self.ultimo = None
        elif nodo == self.primero:  # primer nodo
            self.primero = self.primero.siguiente
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero
        elif nodo == self.ultimo:  # ultimo nodo
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = self.primero
            self.primero.anterior = self.ultimo
        else:  # nodo medio
            nodo.anterior.siguiente = nodo.siguiente
            nodo.siguiente.anterior = nodo.anterior

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
        if self.vacia():
            print('La lista está vacía')
            return
        aux = self.primero
        while True:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break

    # Funcion para graficar Estrucutura
    def graficar(self, filename='lista_circular_doble'):
        if self.vacia():
            print(' ** La lista está vacía, no hay nada que graficar ** ')
            return

        dot = ["digraph G {"]
        dot.append("rankdir=LR;")
        dot.append("node [shape=record];")

        aux = self.primero
        nodos = []
        conexiones = []

        i = 0
        while True:
            nodos.append(f'nodo{i} [label="{aux.dato}"];')

            # Crear conexiones solo si no es el ultimo nodo
            if aux.siguiente != self.primero:
                conexiones.append(f'nodo{i} -> nodo{i + 1};')
                conexiones.append(f'nodo{i + 1} -> nodo{i};')

            aux = aux.siguiente
            i += 1
            # Romper el ciclo al retornar al nodo inicial
            if aux == self.primero:
                break

        # Hacer los enlaces circulares entre el ultimo y el primero
        if i > 1:  # Si hay mas de un nodo
            conexiones.append(f'nodo{i - 1} -> nodo0;')  # ultimo al primero
            conexiones.append(f'nodo0 -> nodo{i - 1};')  # primero al ultimo

        dot.extend(nodos)
        dot.extend(conexiones)
        dot.append("}")

        # Guardar archivo DOT
        dot_file = f'{filename}.dot'
        with open(dot_file, "w") as file:
            file.write("\n".join(dot))
        # Generar imagen
        os.system(f'dot -Tpng {dot_file} -o {filename}.png')
        print(f'Gráfico generado: {filename}.png')
