from clientes.Lista_Dob import Lista_Dob
from vehiculos.ArbolB import ArbolB
from rutas.Lista_Simp import Lista_Simp

class Viajes:
    def __init__(self, ID: int, lugarOrigen: str, lugarDestino: str, fecha: str,
                 cliente: Lista_Dob, vehiculo: ArbolB, ruta_tomada: Lista_Simp):
        self.__ID = ID
        self.__lugarOrigen = lugarOrigen
        self.__lugarDestino = lugarDestino
        self.__fecha = fecha
        self.__cliente = cliente
        self.__vehiculo = vehiculo
        self.__ruta_tomada = ruta_tomada

    # Getter
    def get_ID(self) -> int:
        return self.__ID

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

    def get_Ruta_Tomada(self) -> Lista_Simp:
        return self.__ruta_tomada

    # Setter
    def set_ID(self, ID: int):
        self.__ID = ID

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

    def set_Ruta_Tomada(self, ruta_tomada: Lista_Simp):
        self.__ruta_tomada = ruta_tomada

    # ToString
    def __str__(self) -> str:
        cliente_info = f"DPI: {self.__cliente['DPI']}, Nombre: {self.__cliente['Nombre']}"
        vehiculo_info = f"Placa: {self.__vehiculo['Placa']}, Marca: {self.__vehiculo['Marca']}"
        return (f'Id: {self.__ID}, '
                f'Lugar Origen: {self.__lugarOrigen}, '
                f'Lugar Destino: {self.__lugarDestino}, '
                f'Fecha: {self.__fecha}, '
                f'Cliente: {cliente_info}, '
                f'Vehiculo: {vehiculo_info}, '
                f'Ruta Tomada: {self.__ruta_tomada}')
