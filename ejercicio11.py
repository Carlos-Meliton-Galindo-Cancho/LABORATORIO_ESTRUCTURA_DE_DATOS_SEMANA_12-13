"""
EJERCICIO 11:   Buscar el mínimo y el máximo

Implementar una función que encuentre el nodo con el valor máximo en el árbol

"""


class Nodo:
    def __init__(self, valor):
        self.valor = valor                                             # Almacena el valor del nodo
        self.izquierda = None                                          # Inicializa el hijo izquierdo como None
        self.derecha = None                                            # Inicializa el hijo derecho como None

def encontrar_maximo(arbol):
    if arbol is None:                                                  # Verifica si el árbol está vacío
        return None
    elif arbol.derecha is None:                                        # Verifica si el nodo actual es el más a la derecha
        return arbol.valor
    else:
        return encontrar_maximo(arbol.derecha)                         # Busca recursivamente en el subárbol derecho

# Creamos un árbol de ejemplo
arbol = Nodo(10)                                                       # Creamos el nodo raíz con valor 10
arbol.izquierda = Nodo(5)                                              # Creamos el hijo izquierdo del nodo raíz con valor 5
arbol.derecha = Nodo(15)                                               # Creamos el hijo derecho del nodo raíz con valor 15
arbol.izquierda.izquierda = Nodo(3)                                    # Creamos un nodo con valor 3 como hijo izquierdo del nodo con valor 5
arbol.izquierda.derecha = Nodo(7)                                      # Creamos un nodo con valor 7 como hijo derecho del nodo con valor 5
arbol.derecha.izquierda = Nodo(12)                                     # Creamos un nodo con valor 12 como hijo izquierdo del nodo con valor 15
arbol.derecha.derecha = Nodo(18)                                       # Creamos un nodo con valor 18 como hijo derecho del nodo con valor 15

maximo_valor = encontrar_maximo(arbol)                                 # Encontramos el nodo con el valor máximo en el árbol
print("El valor máximo en el árbol es:", maximo_valor)



"""
LA IMPRESIÓN FINAL SERÁ:

El valor máximo en el árbol es: 18

"""