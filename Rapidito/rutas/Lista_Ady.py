from rutas.Rutas import Ruta
import os

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
            self.__adyacencia[origen] = {}
        self.__adyacencia[origen][destino] = tiempo

        # Agregar la conexion inversa para grafos no dirigidos
        if destino not in self.__adyacencia:
            self.__adyacencia[destino] = {}
        self.__adyacencia[destino][origen] = tiempo

    # Funcion para mostrar la lista adyacencia
    def mostrar_adyacencia(self):
        for nodo, conexiones in self.__adyacencia.items():
            print(f'{nodo}: {conexiones}')

    # Funcion para graficar Mapa
    def graficar(self, filename="grafo"):
        if not self.__adyacencia:
            print("El grafo está vacío, no hay nada que graficar.")
            return

        # Crear el codigo DOT
        dot = ["graph Rutas {"]
        for origen, destinos in self.__adyacencia.items():
            for destino, tiempo in destinos.items():
                if origen < destino:  # Evitar duplicados en grafos no dirigidos
                    dot.append(f'  "{origen}" -- "{destino}" [label="{tiempo}"];')
        dot.append("}")

        # Guardar archivo DOT
        dot_file = f"{filename}.dot"
        with open(dot_file, "w") as file:
            file.write("\n".join(dot))

        # Generar imagen PNG
        os.system(f"dot -Tpng {dot_file} -o {filename}.png")
        print(f"Gráfico generado: {filename}.png")
