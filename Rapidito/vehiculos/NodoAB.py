class NodoAB:
    def __init__(self, orden):
        self.orden = orden
        self.claves = [] # Lista de objeto vehiculo
        self.hijos = [] # lista de punteros hijos
        self.hoja =True # indica si es hoja

    def insertar_en_nodo(self, vehiculo):
        self.claves.append(vehiculo)
        self.claves.sort(key=lambda v: v.get_Placa()) # Ordenar por placa