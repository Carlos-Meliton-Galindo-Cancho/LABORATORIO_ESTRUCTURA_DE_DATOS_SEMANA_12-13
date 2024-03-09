"""
EJERCICIO 9:   Calcular altura y profundidad

Implementar una función que calcule la profundidad de un nodo (la longitud del camino desde la raíz hasta el nodo)

"""


class Nodo:
    def __init__(self, valor):
        self.valor = valor                                                                                 # Almacena el valor del nodo
        self.izquierda = None                                                                              # Inicializa el hijo izquierdo como None
        self.derecha = None                                                                                # Inicializa el hijo derecho como None

def calcular_profundidad(arbol, valor_nodo, profundidad_actual=0):
    if arbol is None:                                                                                      # Verifica si el árbol está vacío
        return None
    elif arbol.valor == valor_nodo:                                                                        # Verifica si el nodo actual es el nodo buscado
        return profundidad_actual
    else:
        profundidad_izquierda = calcular_profundidad(arbol.izquierda, valor_nodo, profundidad_actual + 1)  # Busca recursivamente en los subárboles izquierdo y derecho
        profundidad_derecha = calcular_profundidad(arbol.derecha, valor_nodo, profundidad_actual + 1)
        return profundidad_izquierda if profundidad_izquierda is not None else profundidad_derecha         # Retorna la profundidad encontrada en el subárbol izquierdo o derecho, si es que se encuentra

# Creamos un árbol de ejemplo
arbol = Nodo(1)                                                                                            # Creamos el nodo raíz con valor 1
arbol.izquierda = Nodo(2)                                                                                  # Creamos el hijo izquierdo del nodo raíz con valor 2
arbol.derecha = Nodo(3)                                                                                    # Creamos el hijo derecho del nodo raíz con valor 3
arbol.izquierda.izquierda = Nodo(4)                                                                        # Creamos un nodo con valor 4 como hijo izquierdo del nodo con valor 2
arbol.izquierda.derecha = Nodo(5)                                                                          # Creamos un nodo con valor 5 como hijo derecho del nodo con valor 2
arbol.derecha.izquierda = Nodo(6)                                                                          # Creamos un nodo con valor 6 como hijo izquierdo del nodo con valor 3
arbol.derecha.derecha = Nodo(7)                                                                            # Creamos un nodo con valor 7 como hijo derecho del nodo con valor 3

valor_nodo = 5                                                                                             # Valor del nodo para el cual queremos calcular la profundidad

profundidad_nodo = calcular_profundidad(arbol, valor_nodo)                                                 # Calculamos la profundidad del nodo con el valor especificado

if profundidad_nodo is not None:
    print(f"La profundidad del nodo con valor {valor_nodo} es {profundidad_nodo}.")                        # Imprimimos la profundidad del nodo
else:
    print(f"No se encontró el nodo con valor {valor_nodo} en el árbol.")



"""
LA IMPRESIÓN FINAL SERÁ:

La profundidad del nodo con valor 5 es 2.

"""