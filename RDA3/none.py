
# Implementación de Lista Enlazada Simple

class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        # print(f"Creando nodo con dato: {dato}")

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def insertar_al_final(self, dato):
        nuevo = NodoSimple(dato)
        if not self.cabeza:
            self.cabeza = nuevo
            print(f"Insertando {dato} como cabeza de la lista")
        else:
            actual = self.cabeza
            while actual.siguiente:
                print(f"Recorriendo nodo con dato: {actual.dato}")
                print(f"Actual: {actual.dato}, Siguiente: {actual.siguiente.dato}")
                actual = actual.siguiente
            actual.siguiente = nuevo
            # print(actual.dato)
            print(f"Insertando {dato} al final de la lista")
        # print(dato,end="<->")

#     def mostrar(self):
#         actual = self.cabeza
#         while actual:
#             print(f"[{actual.dato}]", end=" -> ")
#             actual = actual.siguiente
#         print("NULL")


# Uso de la Lista Enlazada Simple
# nsimple= NodoSimple("A")

lista = ListaSimple()
lista.insertar_al_final("A")
lista.insertar_al_final("B")
lista.insertar_al_final("C")
lista.insertar_al_final("D")
# lista.mostrar()