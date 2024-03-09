"""
EJERCICIO 1:  Verificar si una palabra es palíndroma

Implementa una función que determine si una palabra es palíndroma o no. Utiliza una cola para comparar los caracteres de la palabra en orden original y reverso

"""


from collections import deque                                    # Importamos la clase deque del módulo collections para usar una cola

def es_palindroma(palabra):                                      # Definimos una función llamada es_palindroma que toma una palabra como argumento
    cola = deque()                                               # Creamos una cola vacía utilizando la clase deque del módulo collections

    for letra in palabra:                                        # Iteramos sobre cada letra en la palabra
        cola.append(letra)                                       # Añadimos cada letra a la cola

    while len(cola) > 1:                                         # Mientras la longitud de la cola sea mayor que 1 (si es 0 o 1, la palabra es palíndroma)
        if cola.popleft() != cola.pop():                         # Comparamos el primer elemento de la cola (que es el primer carácter de la palabra original) con el último elemento de la cola (que es el último carácter de la palabra original) 
            return False                                         # Si son diferentes, la palabra no es palíndroma
    return True                                                  # Si todos los caracteres coinciden, la palabra es palíndroma

palabra = "reconocer"                                            # Definimos la palabra que queremos verificar si es palíndroma o no
if es_palindroma(palabra):                                       # Llamamos a la función es_palindroma con la palabra como argumento
    print(f'La palabra "{palabra}" es palíndroma.')              # Si la función devuelve True, imprimimos que la palabra es palíndroma
else:
    print(f'La palabra "{palabra}" no es palíndroma.')           # Si la función devuelve False, imprimimos que la palabra no es palíndroma



"""
LA IMPRESIÓN FINAL SERÁ:

La palabra "reconocer" es palíndroma.

"""

