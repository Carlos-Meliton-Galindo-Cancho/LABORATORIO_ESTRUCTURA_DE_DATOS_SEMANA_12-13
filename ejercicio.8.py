"""
EJERCICIO 8:   Calcular altura y profundidad

Implementar una función que calcule la altura del árbol (la longitud del camino más largo desde la raíz hasta una hoja)

"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor                                           # Almacena el valor del nodo
        self.izquierda = None                                        # Inicializa el hijo izquierdo como None
        self.derecha = None                                          # Inicializa el hijo derecho como None

def calcular_altura(arbol):
    if arbol is None:                                                # Verifica si el árbol está vacío
        return 0
    else:
        altura_izquierda = calcular_altura(arbol.izquierda)          # Recursivamente calcula la altura del subárbol izquierdo y derecho
        altura_derecha = calcular_altura(arbol.derecha)
        return max(altura_izquierda, altura_derecha) + 1             # Retorna la altura más grande entre los subárboles izquierdo y derecho, más 1 para el nodo actual

# Creamos un árbol de ejemplo
arbol = Nodo(1)                                                      # Creamos el nodo raíz con valor 1
arbol.izquierda = Nodo(2)                                            # Creamos el hijo izquierdo del nodo raíz con valor 2
arbol.derecha = Nodo(3)                                              # Creamos el hijo derecho del nodo raíz con valor 3
arbol.izquierda.izquierda = Nodo(4)                                  # Creamos un nodo con valor 4 como hijo izquierdo del nodo con valor 2
arbol.izquierda.derecha = Nodo(5)                                    # Creamos un nodo con valor 5 como hijo derecho del nodo con valor 2
arbol.derecha.izquierda = Nodo(6)                                    # Creamos un nodo con valor 6 como hijo izquierdo del nodo con valor 3
arbol.derecha.derecha = Nodo(7)                                      # Creamos un nodo con valor 7 como hijo derecho del nodo con valor 3

# Calculamos la altura del árbol
altura_arbol = calcular_altura(arbol)                                # Llamamos a la función calcular_altura con el árbol creado
print("Altura del árbol:", altura_arbol)                             # Imprimimos la altura del árbol



"""
LA IMPRESIÓN FINAL SERÁ:

Altura del árbol: 3

"""