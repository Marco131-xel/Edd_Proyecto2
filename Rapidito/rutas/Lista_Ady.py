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

    # Metodo para obtener la lista
    def obtener_adyacencia(self):
        return self.__adyacencia

    # Funcion para graficar Mapa
    def graficar(self, filename="grafo"):
        if not self.__adyacencia:
            print("El grafo está vacio, no hay nada que graficar.")
            return
        dot = [
            "graph Rutas {",
            '  bgcolor="#17202a";',
            '  node [style=filled, fillcolor="#145a32", fontcolor="white", shape=circle, width=1.4, fixedsize=true];',
            '  edge [color="white", fontcolor="white"];',
            '  splines=true;',
            '  overlap=false;',
            '  layout=neato;',
        ]
        for origen, destinos in self.__adyacencia.items():
            for destino, tiempo in destinos.items():
                if origen < destino:
                    dot.append(f'  "{origen}" -- "{destino}" [label="{tiempo}", fontsize=10, fontcolor="green"];')

        dot.append("}")
        dot_file = f"{filename}.dot"
        with open(dot_file, "w") as file:
            file.write("\n".join(dot))

        # Crear el grafico PNG
        os.system(f"dot -Tpng {dot_file} -o {filename}.png")
        print(f"Grafico generado: {filename}.png")