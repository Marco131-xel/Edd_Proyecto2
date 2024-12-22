from clientes.Lista_Dob import Lista_Dob
from vehiculos.ArbolB import ArbolB

class Viajes:
    def __init__(self, lugarOrigen: str, lugarDestino: str, fecha: str,
                 cliente: Lista_Dob, vehiculo: ArbolB, ruta_tomada: str): # Ruta tomada es un lista simple FALTA
        self.__lugarOrigen = lugarOrigen
        self.__lugarDestino = lugarDestino
        self.__fecha = fecha
        self.__cliente = cliente
        self.__vehiculo = vehiculo
        self.__ruta_tomada = ruta_tomada

    # Getter
    def get_LugarOrigen(self) -> str:
        return self.__lugarOrigen
    def get_LugarDestino(self) -> str:
        return self.__lugarDestino
    def get_Fecha(self) -> str:
        return self.__fecha
    def get_Cliente(self) -> Lista_Dob:
        return self.__cliente
    def get_Vehiculo(self) -> ArbolB:
        return self.__vehiculo
    def get_Ruta_Tomada(self) -> str:
        return self.__ruta_tomada

    # Setter
    def set_LugarOrigen(self, lugarOrigen: str):
        self.__lugarOrigen = lugarOrigen

    def set_LugarDestino(self, lugarDestino: str):
        self.__lugarDestino = lugarDestino

    def set_Fecha(self, fecha: str):
        self.__fecha = fecha

    def set_Cliente(self, cliente: Lista_Dob):
        self.__cliente = cliente

    def set_Vehiculo(self, vehiculo: ArbolB):
        self.__vehiculo = vehiculo

    def set_Ruta_Tomada(self, ruta_tomada: str):
        self.__ruta_tomada = ruta_tomada

    # ToString
    def __str__(self) -> str:
        return (f'Lugar Origen: {self.__lugarOrigen}, '
                f'Lugar Destino: {self.__lugarDestino}, '
                f'Fecha: {self.__fecha}, '
                f'Cliente: {self.__cliente}, '
                f'Vehiculo: {self.__vehiculo}, '
                f'Ruta Tomada: {self.__ruta_tomada}')