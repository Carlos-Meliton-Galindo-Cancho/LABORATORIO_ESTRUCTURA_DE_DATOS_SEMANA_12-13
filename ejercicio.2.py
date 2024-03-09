"""
EJERCICIO 2:  Diseño de un sistema de gestión de pedidos

Crea un sistema de gestión de pedidos que utilice una cola para procesar los pedidos en el orden en que 
fueron recibidos. Implementa funciones para agregar pedidos, procesar pedidos y mostrar el estado 
actual de la cola

"""


class Pedido:                                                                               # Definición de la clase Pedido para representar un pedido
    def __init__(self, id_pedido, descripcion):                                             # Constructor de la clase Pedido
        self.id_pedido = id_pedido                                                          # Asigna el ID del pedido
        self.descripcion = descripcion                                                      # Asigna la descripción del pedido

class SistemaGestionPedidos:                                                                # Definición de la clase SistemaGestionPedidos para gestionar los pedidos
    def __init__(self):                                                                     # Constructor de la clase SistemaGestionPedidos
        self.cola_pedidos = []                                                              # Inicializa una cola vacía para almacenar los pedidos

    def agregar_pedido(self, pedido):                                                       # Método para agregar un pedido a la cola
        self.cola_pedidos.append(pedido)                                                    # Añade el pedido a la cola

    def procesar_pedido(self):                                                              # Método para procesar el pedido más antiguo de la cola
        if self.cola_pedidos:                                                               # Verifica si la cola de pedidos no está vacía
            return self.cola_pedidos.pop(0)                                                 # Elimina y retorna el primer elemento de la cola (el pedido más antiguo)
        else:
            return "No hay pedidos para procesar"                                           # Retorna un mensaje si la cola está vacía

    def mostrar_estado_cola(self):                                                          # Método para mostrar el estado actual de la cola de pedidos
        if self.cola_pedidos:                                                               # Verifica si la cola de pedidos no está vacía
            print("Estado actual de la cola de pedidos:")
            for pedido in self.cola_pedidos:                                                # Itera sobre cada pedido en la cola
                print(f"ID Pedido: {pedido.id_pedido}, Descripción: {pedido.descripcion}")
        else:
            print("La cola de pedidos está vacía")                                          # Imprime un mensaje si la cola está vacía

sistema = SistemaGestionPedidos()                                                           # Creación de una instancia de la clase SistemaGestionPedidos

pedido1 = Pedido(1, "Producto A")
pedido2 = Pedido(2, "Producto B")                                                           # Creación de algunos pedidos de ejemplo
pedido3 = Pedido(3, "Producto C")

sistema.agregar_pedido(pedido1)
sistema.agregar_pedido(pedido2)                                                             # Agregar los pedidos a la cola
sistema.agregar_pedido(pedido3)

sistema.mostrar_estado_cola()                                                               # Mostrar el estado actual de la cola de pedidos 

pedido_procesado = sistema.procesar_pedido()                                                # Procesar un pedido de la cola
print(f"Pedido procesado: ID {pedido_procesado.id_pedido}, Descripción: {pedido_procesado.descripcion}")

sistema.mostrar_estado_cola()                                                               # Mostrar el estado actual de la cola de pedidos después de procesar un pedido 



"""
LA IMPRESIÓN FINAL SERÁ:

Estado actual de la cola de pedidos:
ID Pedido: 1, Descripción: Producto A
ID Pedido: 2, Descripción: Producto B
ID Pedido: 3, Descripción: Producto C
Pedido procesado: ID 1, Descripción: Producto A
Estado actual de la cola de pedidos:
ID Pedido: 2, Descripción: Producto B
ID Pedido: 3, Descripción: Producto C

"""