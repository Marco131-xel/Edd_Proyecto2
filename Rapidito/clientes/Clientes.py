class Clientes:
    # Constructor
    def __init__(self, DPI:int, nombre: str, apellido: str, genero: str, telefono: int , direccion: str):
        self.DPI = DPI
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.telefono = telefono
        self.direccion = direccion

    # Getter
    def get_DPI(self):
        return self.DPI
    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido
    def get_genero(self):
        return self.genero
    def get_telefono(self):
        return self.telefono
    def get_direccion(self):
        return self.direccion

    # Setter
    def set_DPI(self, DPI: int):
        self.DPI = DPI
    def set_nombre(self, nombre: str):
        self.nombre = nombre
    def set_apellido(self, apellido: str):
        self.apellido = apellido
    def set_genero(self, genero: str):
        self.genero = genero
    def set_telefono(self, telefono: int):
        self.telefono = telefono
    def set_direccion(self, direccion: str):
        self.direccion = direccion

    # ToString
    def __str__(self) -> str:
        return ()