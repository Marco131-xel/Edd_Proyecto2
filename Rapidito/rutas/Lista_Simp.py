from rutas.NodoLS import NodoLS
from rutas.Rutas import Ruta

class Lista_Simp:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self) -> bool:
        return self.primero is None

    def agregar_ultimo(self, ruta: Ruta):
        nuevo_nodo = NodoLS(ruta)
        if self.vacia():
            self.primero = self.ultimo = nuevo_nodo
        else :
            self.ultimo.siquiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def agregar_primero(self, ruta: Ruta):
        nuevo_nodo = NodoLS(ruta)
        if self.vacia():
            self.primero = self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.siquiente = self.primero
            self.primero = nuevo_nodo

    def eliminar_ultimo(self):
        if self.vacia():
            print('La lista esta vacia')
            return
        if self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            aux = self.primero
            while aux.siguiente != self.ultimo:
                aux = aux.siguiente
            aux.siquiente = None
            self.ultimo = aux

    def eliminar_inicio(self):
        if self.vacia():
            print('La lista esta vacia')
            return
        if self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente

    def recorrido(self):
        aux = self.primero
        while aux is not None:
            print(aux)
            aux = aux.siquiente

    def buscar_origen(self, origen: str):
        aux = self.primero
        while aux is not None:
            if aux.ruta.get_Origen() == origen:
                return aux.ruta
            aux = aux.siquiente
        return None

    def buscar_destino(self, destino: str):
        aux = self.primero
        while aux is not None:
            if aux.ruta.get_Destino() == destino:
                return aux.ruta
            aux = aux.siquiente
        return None

    def agregar(self, ruta: Ruta, prioridad: bool = False):
        if prioridad:
            self.agregar_primero(ruta)
        else:
            self.agregar_ultimo(ruta)

    def eliminar(self, inicio: bool = True):
        if inicio:
            self.eliminar_inicio()
        else:
            self.eliminar_ultimo()

    def __str__(self) -> str:
        rutas = []
        aux = self.primero
        while aux is not None:
            rutas.append(str(aux.ruta))
            aux = aux.siquiente
        return ' -> '.join(rutas)
