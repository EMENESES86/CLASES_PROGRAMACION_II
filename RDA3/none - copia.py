
# Implementación de Lista Enlazada Simple

class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.posterior = None
        # print(f"Creando nodo con dato: {dato}")

class ListaSimple:
    def __init__(self):
        self.primero = None

    def insertar_al_final(self, dato):
        nuevo = NodoSimple(dato)
        if not self.primero:
            self.primero = nuevo
            print(f"Insertando {dato} como primero de la lista")
        else:
            actual = self.primero
            while actual.posterior:
                actual = actual.posterior
                actual.posterior = nuevo
            print(f"Recorriendo nodo con dato: {actual.posterior}")
            # print(nuevo.dato)
            print(f"Insertando {dato} al final de la lista")
        # print(dato,end="<->")

    # def mostrar(self):
    #     actual = self.cabeza

    #     while actual:
    #         print(f"[{actual.dato}]", end=" -> ")
    #         actual = actual.posterior
    #     print("NULL")




lista = ListaSimple()
lista.insertar_al_final("A")
lista.insertar_al_final("B")
lista.insertar_al_final("C")
lista.insertar_al_final("D")
# lista.mostrar()