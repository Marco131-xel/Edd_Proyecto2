from rutas.Lista_Simp import Lista_Simp
from rutas.Rutas import Ruta

class Grafo:
    def __init__(self, adyacencia):
        self.adyacencia = adyacencia

    def encontrar_rutas(self, origen, destino, ruta_actual=None, rutas=None, visitados=None):
        if ruta_actual is None:
            ruta_actual = Lista_Simp()
        if rutas is None:
            rutas = []
        if visitados is None:
            visitados = set()

        # Agregar el nodo actual a los visitados
        visitados.add(origen)

        # Agregar el nodo actual a la ruta
        if ruta_actual.buscar_origen(origen) is None:
            ruta_actual.agregar_ultimo(Ruta(origen, None, 0))

        # Si llegamos al destino, agregar la ruta a la lista de rutas
        if origen == destino:
            rutas.append(ruta_actual)
            return rutas

        # Explorar los vecinos
        for vecino, tiempo in self.adyacencia.get(origen, {}).items():
            if vecino not in visitados:
                # Crear una nueva ruta para explorar
                nueva_ruta = Lista_Simp()
                aux = ruta_actual.primero
                while aux is not None:
                    nueva_ruta.agregar_ultimo(aux.ruta)
                    aux = aux.siquiente
                nueva_ruta.agregar_ultimo(Ruta(origen, vecino, tiempo))

                # Recursivamente explorar desde el vecino
                self.encontrar_rutas(vecino, destino, nueva_ruta, rutas, visitados.copy())
        return rutas

    # Funcion calcular tiempo
    def calcular_tiempos(self, rutas):
        tiempos = []
        for ruta in rutas:
            tiempo_total = 0
            aux = ruta.primero
            while aux.siquiente is not None:
                tiempo_total += int(aux.siquiente.ruta.get_Tiempo())
                aux = aux.siquiente
            tiempos.append((ruta, tiempo_total))
        return tiempos

    def obtener_ruta_min_max(self, tiempos):
        min_ruta = min(tiempos, key=lambda x: x[1])
        max_ruta = max(tiempos, key=lambda x: x[1])
        return min_ruta, max_ruta
