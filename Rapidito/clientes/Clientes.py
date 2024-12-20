class Clientes:
    # Constructor
    def __init__(self, dpi: int, nombre: str, apellido: str, genero: str, telefono: int , direccion: str):
        self.__dpi = dpi
        self.__nombre = nombre
        self.__apellido = apellido
        self.__genero = genero
        self.__telefono = telefono
        self.__direccion = direccion

    # Getter
    def get_Dpi(self) -> int:
        return self.__dpi

    def get_Nombre(self) -> str:
        return self.__nombre

    def get_Apellido(self) -> str:
        return self.__apellido

    def get_Genero(self) -> str:
        return self.__genero

    def get_Telefono(self) -> int:
        return self.__telefono

    def get_Direccion(self)->str:
        return self.__direccion

    # Setter
    def set_Dpi(self, dpi: int):
        self.__dpi = dpi

    def set_Nombre(self, nombre: str):
        self.__nombre = nombre

    def set_Apellido(self, apellido: str):
        self.__apellido = apellido

    def set_Genero(self, genero: str):
        self.__genero = genero

    def set_Telefono(self, telefono: int):
        self.__telefono = telefono

    def set_Direccion(self, direccion: str):
        self.__direccion = direccion

    # ToString
    def __str__(self) -> str:
        return (f'DPI: {self.__dpi}, '
                f'Nombre: {self.__nombre}, '
                f'Apellido: {self.__apellido}, '
                f'Genero: {self.__genero}, '
                f'Telefono: {self.__telefono}, '
                f'Direccion: {self.__direccion}')