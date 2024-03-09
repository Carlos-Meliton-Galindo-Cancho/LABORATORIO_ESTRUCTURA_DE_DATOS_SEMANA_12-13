"""
EJERCICIO 5:   Contar nodos

 Implementar una función que cuente la cantidad de nodos en el árbol

"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor                                                     # Almacena el valor del nodo
        self.izquierda = None                                                  # Inicializa el hijo izquierdo como None
        self.derecha = None                                                    # Inicializa el hijo derecho como None

def contar_nodos(arbol):
    if arbol is None:                                                          # Verifica si el árbol está vacío
        return 0
    else:
        return 1 + contar_nodos(arbol.izquierda) + contar_nodos(arbol.derecha) # Recursivamente cuenta los nodos en el subárbol izquierdo y derecho y suma 1 para el nodo actual

# Creamos un árbol de ejemplo
arbol = Nodo(1)                                                                # Creamos el nodo raíz con valor 1
arbol.izquierda = Nodo(2)                                                      # Creamos el hijo izquierdo del nodo raíz con valor 2
arbol.derecha = Nodo(3)                                                        # Creamos el hijo derecho del nodo raíz con valor 3
arbol.izquierda.izquierda = Nodo(4)                                            # Creamos un nodo con valor 4 como hijo izquierdo del nodo con valor 2
arbol.izquierda.derecha = Nodo(5)                                              # Creamos un nodo con valor 5 como hijo derecho del nodo con valor 2
arbol.derecha.izquierda = Nodo(6)                                              # Creamos un nodo con valor 6 como hijo izquierdo del nodo con valor 3
arbol.derecha.derecha = Nodo(7)                                                # Creamos un nodo con valor 7 como hijo derecho del nodo con valor 3

# Contamos los nodos en el árbol
cantidad_nodos = contar_nodos(arbol)                                           # Llamamos a la función contar_nodos con el árbol creado
print("Cantidad de nodos en el árbol:", cantidad_nodos)                        # Imprimimos la cantidad total de nodos en el árbol



"""
LA IMPRESIÓN FINAL SERÁ:

Cantidad de nodos en el árbol: 7

"""