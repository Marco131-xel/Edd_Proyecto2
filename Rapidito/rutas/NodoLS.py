from rutas.Rutas import Ruta

class NodoLS:
    def __init__(self, ruta: Ruta):
        self.ruta = ruta
        self.siquiente = None

    def __str__(self) -> str:
        return str(self.ruta)