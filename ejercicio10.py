"""
EJERCICIO 10:   Buscar el mínimo y el máximo

Implementar una función que encuentre el nodo con el valor mínimo en el árbol

"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor                                           # Almacena el valor del nodo
        self.izquierda = None                                        # Inicializa el hijo izquierdo como None
        self.derecha = None                                          # Inicializa el hijo derecho como None

def encontrar_minimo(arbol):
    if arbol is None:                                                # Verifica si el árbol está vacío
        return None
    elif arbol.izquierda is None:                                    # Verifica si el nodo actual es el más a la izquierda
        return arbol.valor
    else:
        return encontrar_minimo(arbol.izquierda)                     # Busca recursivamente en el subárbol izquierdo

# Creamos un árbol de ejemplo
arbol = Nodo(10)                                                     # Creamos el nodo raíz con valor 10
arbol.izquierda = Nodo(5)                                            # Creamos el hijo izquierdo del nodo raíz con valor 5
arbol.derecha = Nodo(15)                                             # Creamos el hijo derecho del nodo raíz con valor 15
arbol.izquierda.izquierda = Nodo(3)                                  # Creamos un nodo con valor 3 como hijo izquierdo del nodo con valor 5
arbol.izquierda.derecha = Nodo(7)                                    # Creamos un nodo con valor 7 como hijo derecho del nodo con valor 5
arbol.derecha.izquierda = Nodo(12)                                   # Creamos un nodo con valor 12 como hijo izquierdo del nodo con valor 15
arbol.derecha.derecha = Nodo(18)                                     # Creamos un nodo con valor 18 como hijo derecho del nodo con valor 15

minimo_valor = encontrar_minimo(arbol)                               # Encontramos el nodo con el valor mínimo en el árbol
print("El valor mínimo en el árbol es:", minimo_valor)



"""
LA IMPRESIÓN FINAL SERÁ:

El valor mínimo en el árbol es: 3

"""