class Ruta:
    def __init__(self, origen: str, destino: str, tiempo: int):
        self.__origen = origen
        self.__destino = destino
        self.__tiempo = tiempo

    # Getter
    def get_Origen(self) -> str:
        return self.__origen

    def get_Destino(self) -> str:
        return self.__destino

    def get_Tiempo(self) -> int:
        return self.__tiempo

    # Setter
    def set_Origen(self, origen: str):
        self.__origen = origen

    def set_Destino(self, destino: str):
        self.__destino = destino

    def set_Tiempo(self, tiempo: int):
        self.__tiempo = tiempo

    # ToString
    def __str__(self) -> str:
        return (f'Origen: {self.__origen}, '
                f'Destino: {self.__destino}, '
                f'Tiempo: {self.__tiempo}')