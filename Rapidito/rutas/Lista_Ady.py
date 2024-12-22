from rutas.Rutas import Ruta
class Lista_Ady:
    def __init__(self):
        self.__adyacencia = {}

    # Funcion para agregar una ruta al grafo
    def agregar_ruta(self, ruta: Ruta):
        origen = ruta.get_Origen()
        destino = ruta.get_Destino()
        tiempo = ruta.get_Tiempo()

        # Agregar conexion desde el origen al destino
        if origen not in self.__adyacencia:
            self.__adyacencia[origen] = ''
        if destino not in self.__adyacencia[origen]:
            self.__adyacencia[origen] += (',' + f'{destino}:{tiempo}' if self.__adyacencia[origen]
                                          else f'{destino}:{tiempo}')

        # Agregar la conexion inversa para grafos no dirigidos
        if destino not in self.__adyacencia:
            self.__adyacencia[destino] = ''
        if origen not in self.__adyacencia[destino]:
            self.__adyacencia[destino] += (',' + f'{origen}:{tiempo}' if self.__adyacencia[destino]
                                           else f'{origen}:{tiempo}')

    # Funcion para mostrar la lista adyacencia
    def mostrar_adyacencia(self):
        for nodo, conexiones in self.__adyacencia.items():
            print(f'{nodo}: {conexiones}')