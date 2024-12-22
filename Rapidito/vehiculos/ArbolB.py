from vehiculos.NodoAB import NodoAB
#from vehiculos.Vehiculos import Vehiculos
import os

class ArbolB:
    def __init__(self):
        self.orden = 5 # arbol de orden 5
        self.raiz = NodoAB(self.orden)

                # METODOS PRINCIPALES
    # Funcion para insertar vehiculos
    def insertar(self, Vehiculos):
        nodo_raiz = self.raiz
        if len(nodo_raiz.claves) == (2 * self.orden) - 1:
            nuevo_nodo = NodoAB(self.orden)
            self.raiz = nuevo_nodo
            nuevo_nodo.hoja = False
            nuevo_nodo.hijos.append(nodo_raiz)
            self.dividir_nodo(nuevo_nodo, 0)
            self.insertar_no_lleno(nuevo_nodo, Vehiculos)
        else:
            self.insertar_no_lleno(nodo_raiz, Vehiculos)

    # Funcion para buscar vehiculos por su placa
    def buscar(self, placa, nodo = None):
        if nodo is None:
            nodo = self.raiz
        for i, Vehiculos in enumerate(nodo.claves):
            if placa == Vehiculos.get_Placa():
                return Vehiculos
            elif placa < Vehiculos.get_Placa() and not nodo.hoja:
                return self.buscar(placa, nodo.hijos[i])

        if not nodo.hoja:
            return self.buscar(placa, nodo.hijos[-1])

        return None

    # Funcion para modificar un vehiculo por su placa
    def modificar(self, placa, nueva_marca, nuevo_modelo, nuevo_precio):
        Vehiculos = self.buscar(placa)
        if Vehiculos:
            Vehiculos.set_Marca(nueva_marca)
            Vehiculos.set_Modelo(nuevo_modelo)
            Vehiculos.set_Precio(nuevo_precio)
            return True
        return False

    # Funcion para eliminar un vehiculo por su placa
    def eliminar(self, placa):
        self.eliminar_clave(self.raiz, placa)
        if len(self.raiz.claves) == 0 and not self.raiz.hoja:
            self.raiz = self.raiz.hijos[0]

    # Funcion para mostrar un vehiculo por su placa
    def mostrar(self, placa):
        Vehiculos = self.buscar(placa)
        if Vehiculos:
            return str(Vehiculos)
        return 'vehiculo no encontrado'

    # Funcion para llenar el arbol vacio
    def insertar_no_lleno(self, nodo, Vehiculos):
        if nodo.hoja:
            nodo.insertar_en_nodo(Vehiculos)
        else:
            i = len(nodo.claves) - 1
            while i >= 0 and Vehiculos.get_Placa() < nodo.claves[i].get_Placa():
                i -= 1
            i += 1
            if len(nodo.hijos[i].claves) == (2 * self.orden) - 1:
                self.dividir_nodo(nodo, i)
                if Vehiculos.get_Placa() > nodo.claves[i].get_Placa():
                    i += 1
            self.insertar_no_lleno(nodo.hijos[i], Vehiculos)

                # METODOS AUXILIARES
    # Funcion para dividir un nodo hijo lleno de nodos y ajusta al nodo padre
    def dividir_nodo(self, nodo_padre, indice):
        orden = self.orden
        nodo_hijo = nodo_padre.hijos[indice]
        nuevo_nodo = NodoAB(orden)
        nuevo_nodo.hoja = nodo_hijo.hoja

        nodo_padre.claves.insert(indice, nodo_hijo.claves[orden - 1])
        nodo_padre.hijos.insert(indice + 1, nuevo_nodo)

        nuevo_nodo.claves = nodo_hijo.claves[orden:]
        nodo_hijo.claves = nodo_hijo.claves[:orden - 1]

        if not nodo_hijo.hoja:
            nuevo_nodo.hijos = nodo_hijo.hijos[orden:]
            nodo_hijo.hijos = nodo_hijo.hijos[:orden]

    # Funcion eliminar clave
    def eliminar_clave(self, nodo, clave):
        if clave in nodo.claves:
            if nodo.hoja:
                nodo.claves.remove(clave)
            else:
                indice = nodo.claves.index(clave)
                if len(nodo.hijos[indice].claves) >= self.orden:
                    predecesor = self.obtener_predecesor(nodo.hijos[indice])
                    nodo.claves[indice] = predecesor
                    self.eliminar_clave(nodo.hijos[indice], predecesor)
                elif len(nodo.hijos[indice + 1].claves) >= self.orden:
                    sucesor = self.obtener_sucesor(nodo.hijos[indice + 1])
                    nodo.claves[indice] = sucesor
                    self.eliminar_clave(nodo.hijos[indice + 1], sucesor)
                else:
                    self.fusionar_nodos(nodo, indice)
                    self.eliminar_clave(nodo.hijos[indice], clave)
        else:
            if nodo.hoja:
                return
            indice = 0
            while indice < len(nodo.claves) and clave > nodo.claves[indice]:
                indice += 1
            if len(nodo.hijos[indice].claves) < self.orden:
                self.reforzar_hijo(nodo, indice)
            self.eliminar_clave(nodo.hijos[indice], clave)

    # Funcion predecesor del nodo
    def obtener_predecesor(self, nodo):
        while not nodo.hoja:
            nodo = nodo.hijos[-1]
        return nodo.claves[-1]
    # Funcion sucesor del nodo
    def obtener_sucesor(self, nodo):
        while not nodo.hoja:
            nodo = nodo.hijos[0]
        return nodo.claves[0]

    # Funcion fusionar nodos
    def fusionar_nodos(self, nodo, indice):
        hijo_izq = nodo.hijos[indice]
        hijo_der = nodo.hijos[indice + 1]
        clave_media = nodo.claves.pop(indice)
        hijo_izq.claves.append(clave_media)
        hijo_izq.claves.extend(hijo_der.claves)
        if not hijo_der.hoja:
            hijo_izq.hijos.extend(hijo_der.hijos)
        nodo.hijos.pop(indice + 1)

    # Funcion reforzar el nodo hijo
    def reforzar_hijo(self, nodo, indice):
        if indice > 0 and len(nodo.hijos[indice - 1].claves) >= self.orden:
            hijo = nodo.hijos[indice]
            hermano_izq = nodo.hijos[indice - 1]
            clave_padre = nodo.claves[indice - 1]
            hijo.claves.insert(0, clave_padre)
            nodo.claves[indice - 1] = hermano_izq.claves.pop(-1)
            if not hermano_izq.hoja:
                hijo.hijos.insert(0, hermano_izq.hijos.pop(-1))
        elif indice < len(nodo.hijos) - 1 and len(nodo.hijos[indice + 1].claves) >= self.orden:
            hijo = nodo.hijos[indice]
            hermano_der = nodo.hijos[indice + 1]
            clave_padre = nodo.claves[indice]
            hijo.claves.append(clave_padre)
            nodo.claves[indice] = hermano_der.claves.pop(0)
            if not hermano_der.hoja:
                hijo.hijos.append(hermano_der.hijos.pop(0))
        else:
            if indice < len(nodo.hijos) - 1:
                self.fusionar_nodos(nodo, indice)
            else:
                self.fusionar_nodos(nodo, indice - 1)

    # Funcion para imprimir el arbol
    def imprimir(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz
            print('Nivel', nivel, ':', nodo.claves)
        if not nodo.hoja:
            for hijo in nodo.hijos:
                self.imprimir(hijo, nivel + 1)

    # Funcion para graficar Estructura
    def graficar(self, filename='arbol_b'):
        if not self.raiz:
            print('** El arbol esta vacio, no hay nada que graficar ** ')
            return

        # Crear el codigo DOT
        dot = ["digraph G {"]
        dot.append("node [shape=record];")

        def recorrer_nodo(nodo, indice):
            nodo_id = f"nodo{indice}"
            claves_str = "|".join(str(clave) for clave in nodo.claves)
            dot.append(f'{nodo_id} [label="<p0> |{claves_str}| <p{len(nodo.claves)}>"];')

            if not nodo.hoja:
                for i, hijo in enumerate(nodo.hijos):
                    hijo_id = recorrer_nodo(hijo, len(dot))
                    dot.append(f"{nodo_id}:p{i} -> {hijo_id};")
            return nodo_id

        # Recorrer y construir el arbol en DOT
        recorrer_nodo(self.raiz, 0)

        dot.append("}")

        # Guardar archivo DOT
        dot_file = f"{filename}.dot"
        with open(dot_file, "w") as file:
            file.write("\n".join(dot))

        # Generar imagen
        os.system(f'dot -Tpng {dot_file} -o {filename}.png')
        print(f'Grafico generado: {filename}.png')