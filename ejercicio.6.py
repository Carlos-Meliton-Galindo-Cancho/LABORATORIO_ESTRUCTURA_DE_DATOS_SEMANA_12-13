"""
EJERCICIO 6:   Contar nodos

Implementar una función que cuente la cantidad de nodos hoja (que no tienen hijos)

"""


class Nodo:
    def __init__(self, valor):
        self.valor = valor                                                           # Almacena el valor del nodo
        self.izquierda = None                                                        # Inicializa el hijo izquierdo como None
        self.derecha = None                                                          # Inicializa el hijo derecho como None

def contar_nodos_hoja(arbol):
    if arbol is None:                                                                # Verifica si el árbol está vacío
        return 0
    elif arbol.izquierda is None and arbol.derecha is None:                          # Verifica si el nodo actual es una hoja
        return 1
    else:
        return contar_nodos_hoja(arbol.izquierda) + contar_nodos_hoja(arbol.derecha) # Recursivamente cuenta los nodos hoja en el subárbol izquierdo y derecho

# Creamos un árbol de ejemplo
arbol = Nodo(1)                                                                      # Creamos el nodo raíz con valor 1
arbol.izquierda = Nodo(2)                                                            # Creamos el hijo izquierdo del nodo raíz con valor 2
arbol.derecha = Nodo(3)                                                              # Creamos el hijo derecho del nodo raíz con valor 3
arbol.izquierda.izquierda = Nodo(4)                                                  # Creamos un nodo con valor 4 como hijo izquierdo del nodo con valor 2
arbol.izquierda.derecha = Nodo(5)                                                    # Creamos un nodo con valor 5 como hijo derecho del nodo con valor 2
arbol.derecha.izquierda = Nodo(6)                                                    # Creamos un nodo con valor 6 como hijo izquierdo del nodo con valor 3
arbol.derecha.derecha = Nodo(7)                                                      # Creamos un nodo con valor 7 como hijo derecho del nodo con valor 3

# Contamos los nodos hoja en el árbol
cantidad_nodos_hoja = contar_nodos_hoja(arbol)                                       # Llamamos a la función contar_nodos_hoja con el árbol creado
print("Cantidad de nodos hoja en el árbol:", cantidad_nodos_hoja)                    # Imprimimos la cantidad de nodos hoja en el árbol



"""
LA IMPRESIÓN FINAL SERÁ:

Cantidad de nodos hoja en el árbol: 4

"""