from viajes.Nodoviaje import Nodoviaje
import os

class Lista_Sviaje:
    def __init__(self):
        self.primero = None

    def vacia(self):
        return self.primero is None

    # Funcion para crear un viaje
    def crear_viaje(self, viaje):
        nuevo = Nodoviaje(viaje)
        if self.vacia():
            self.primero = nuevo
        else:
            aux = self.primero
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = nuevo

    # Funcion para buscar un viaje por ID
    def buscar_viaje(self, ID):
        aux = self.primero
        while aux is not None:
            if aux.viaje.get_ID() == ID:
                return aux.viaje
            aux = aux.siguiente
        return None

    # Funcion para modificar un viaje por el ID
    def modificar_viaje(self, ID, nuevo_viaje):
        aux = self.primero
        while aux is not None:
            if aux.viaje.get_ID() == ID:
                aux.viaje = nuevo_viaje
                return True
            aux = aux.siguiente
        return False

    # Funcion para mostrar un viaje por ID
    def mostrar_viaje(self, ID):
        viaje = self.buscar_viaje(ID)
        if viaje is not None:
            print(viaje)
        else:
            print(f'Viaje con ID {ID} no existe')

    # Funcion para eliminar un viaje
    def eliminar_viaje(self, ID):
        if self.vacia():
            return False

        if self.primero.viaje.get_ID() == ID:
            self.primero = self.primero.siguiente
            return True

        aux = self.primero
        while aux.siguiente is not None:
            if aux.siguiente.viaje.get_ID() == ID:
                aux.siguiente = aux.siguiente.siguiente
                return True
            aux = aux.siguiente
        return False

    # Funcion para mostrar todos los viajes
    def mostrar_todos(self):
        aux = self.primero
        while aux is not None:
            print(aux.viaje)
            aux = aux.siguiente

    # Funcion para graficar la Estructura con Graphviz
    def graficar(self, filename='lista_viajes'):
        import os

        if self.vacia():
            print(' ** La lista está vacía, no hay nada que graficar ** ')
            return

        # Crear código DOT
        dot = ["digraph G {"]
        dot.append('rankdir=LR;')
        dot.append('bgcolor="#17202a";')
        dot.append('node [shape=record, style=filled, fillcolor="#145a32", fontcolor="white"];')
        dot.append('edge [color="white"];')

        aux = self.primero
        nodos = []
        conexiones = []
        i = 0

        while aux is not None:
            # Formatear cliente y vehículo
            cliente = aux.viaje.get_Cliente()
            vehiculo = aux.viaje.get_Vehiculo()

            cliente_info = f"DPI: {cliente['DPI']}\\nNombre: {cliente['Nombre']}"
            vehiculo_info = f"Placa: {vehiculo['Placa']}\\nMarca: {vehiculo['Marca']}"

            # Crear nodo con los datos formateados
            nodos.append(
                f'nodo{i} [label="'
                f'ID: {aux.viaje.get_ID()}\\n'
                f'Origen: {aux.viaje.get_LugarOrigen()}\\n'
                f'Destino: {aux.viaje.get_LugarDestino()}\\n'
                f'Fecha: {aux.viaje.get_Fecha()}\\n'
                f'Cliente: {cliente_info}\\n'
                f'Vehiculo: {vehiculo_info}\\n'
                f'Ruta: {aux.viaje.get_Ruta_Tomada()}"];'
            )

            # Crear conexión al siguiente nodo
            if aux.siguiente is not None:
                conexiones.append(f'nodo{i} -> nodo{i + 1};')

            aux = aux.siguiente
            i += 1

        # Agregar nodos y conexiones al grafo
        dot.extend(nodos)
        dot.extend(conexiones)
        dot.append("}")

        # Guardar archivo DOT
        dot_file = f'{filename}.dot'
        with open(dot_file, "w") as file:
            file.write("\n".join(dot))

        # Generar imagen usando Graphviz
        os.system(f'dot -Tpng {dot_file} -o {filename}.png')
        print(f'Grafico generado: {filename}.png')
