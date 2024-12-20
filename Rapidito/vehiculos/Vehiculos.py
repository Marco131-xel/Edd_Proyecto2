class Vehiculos:
    #Construcctor
    def __init__(self, placa: str, marca: str, modelo: int, precio: float) :
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio

    # Getter
    def get_Placa(self) -> str :
        return self.__placa

    def get_Marca(self) -> str:
        return self.__marca

    def get_Modelo(self) -> int :
        return self.__modelo

    def get_Precio(self) -> float :
        return self.__precio

    # Setter
    def set_Placa(self, placa: str):
        self.__placa = placa

    def set_Marca(self, marca: str):
        self.__marca = marca

    def set_Modelo(self, modelo: int):
        self.__modelo = modelo

    def set_Precio(self, precio: float):
        self.__precio = precio

    # ToString
    def __str__(self) -> str :
        return (f'Placa: {self.__placa}, '
                f'Marca: {self.__marca}, '
                f'Modelo: {self.__modelo}, '
                f'Precio: {self.__precio:.2f}')