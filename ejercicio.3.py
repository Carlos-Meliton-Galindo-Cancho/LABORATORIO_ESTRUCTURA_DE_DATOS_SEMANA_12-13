"""
EJERCICIO 3:   Búsqueda de rutas en un laberinto

Desarrolla un programa que encuentre el camino más corto a través de un laberinto. Utiliza una cola 
para realizar un recorrido en anchura (BFS) desde el punto de inicio hasta el punto de destino

"""

from collections import deque                                                                        # Importa la clase deque de la librería collections para utilizar una cola

laberinto = [                                                                                        # Definir el laberinto como una matriz bidimensional
    [0, 0, 1, 0, 0],                       
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],                                                                                 # 0 representa un pasillo, 1 representa una pared
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

# Definir las coordenadas de inicio y fin
inicio = (0, 0)                                                                                      # Coordenadas de inicio del laberinto
fin = (4, 4)                                                                                         # Coordenadas de fin del laberinto

# Definir la cola para BFS
cola = deque()                                                                                       # Se crea una cola utilizando deque para realizar BFS
cola.append(inicio)                                                                                  # Se agrega el punto de inicio a la cola para comenzar la búsqueda

# Definir la matriz de visitados para mantener un registro de las celdas visitadas
visitados = [[False] * len(laberinto[0]) for _ in range(len(laberinto))]                             # Se inicializa una matriz de visitados con valores False
visitados[inicio[0]][inicio[1]] = True                                                               # Se marca la celda de inicio como visitada

direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]                                                     # Definir las direcciones para explorar: derecha, izquierda, abajo, arriba

# Búsqueda en anchura (BFS)
while cola:                                                                                          # Mientras la cola no esté vacía
    actual = cola.popleft()                                                                          # Se extrae el primer elemento de la cola para explorar sus vecinos
    if actual == fin:                                                                                # Si se alcanza el punto de destino, se detiene la búsqueda
        break
    
    for direccion in direcciones:                                                                    # Explorar los vecinos de la celda actual
        nueva_posicion = (actual[0] + direccion[0], actual[1] + direccion[1])
        if 0 <= nueva_posicion[0] < len(laberinto) and 0 <= nueva_posicion[1] < len(laberinto[0]):   # Verificar si la nueva posición está dentro de los límites del laberinto y no ha sido visitada
            if not visitados[nueva_posicion[0]][nueva_posicion[1]] and laberinto[nueva_posicion[0]][nueva_posicion[1]] == 0:
                visitados[nueva_posicion[0]][nueva_posicion[1]] = True                               # Marcar la nueva posición como visitada
                cola.append(nueva_posicion)                                                          # Agregar la nueva posición a la cola para explorar sus vecinos
    
# Reconstruir el camino más corto si se encontró uno
if visitados[fin[0]][fin[1]]:                                                                        # Si el punto de destino fue visitado
    camino = []                                                                                      # Se inicializa una lista para almacenar el camino más corto
    actual = fin                                                                                     # Se comienza desde el punto de destino
    while actual != inicio:                                                                          # Mientras no se llegue al punto de inicio
        camino.append(actual)                                                                        # Se añade la celda actual al camino
        for direccion in direcciones:                                                                # Se busca el vecino visitado más cercano hacia el inicio
            nueva_posicion = (actual[0] - direccion[0], actual[1] - direccion[1])
            if 0 <= nueva_posicion[0] < len(laberinto) and 0 <= nueva_posicion[1] < len(laberinto[0]):
                if visitados[nueva_posicion[0]][nueva_posicion[1]]:                                  # Si el vecino fue visitado
                    actual = nueva_posicion                                                          # Se actualiza la celda actual
                    break
    camino.append(inicio)                                                                            # Se añade el punto de inicio al camino
    camino.reverse()                                                                                 # Se invierte el camino para que esté en orden desde el inicio hasta el destino
    print("El camino más corto es:", camino)                                                         # Se imprime el camino más corto
else:
    print("No se encontró ningún camino desde el punto de inicio hasta el punto de destino.")        # Se imprime un mensaje si no se encontró un camino



