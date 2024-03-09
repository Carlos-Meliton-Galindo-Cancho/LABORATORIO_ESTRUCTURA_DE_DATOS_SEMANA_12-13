"""
EJERCICIO 4:   Diseño de un sistema de gestión de tareas (Avanzado)

Implementa un sistema de gestión de tareas que permita agregar tareas, marcar tareas como 
completadas y mostrar la próxima tarea pendiente

"""


class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False                                       # Inicialmente, la tarea se marca como no completada

class SistemaGestionTareas:
    def __init__(self):
        self.lista_tareas = []                                        # Inicializamos una lista vacía para almacenar las tareas

    def agregar_tarea(self, descripcion):
        tarea_nueva = Tarea(descripcion)                              # Creamos una nueva instancia de la clase Tarea
        self.lista_tareas.append(tarea_nueva)                         # Agregamos la tarea a la lista de tareas

    def marcar_completada(self, indice_tarea):
        if 0 <= indice_tarea < len(self.lista_tareas):
            self.lista_tareas[indice_tarea].completada = True         # Marcamos la tarea especificada por su índice como completada
        else:
            print("Índice de tarea inválido")

    def proxima_tarea_pendiente(self):
        for tarea in self.lista_tareas:
            if not tarea.completada:
                return tarea.descripcion                              # Devolvemos la descripción de la primera tarea pendiente
        return "No hay tareas pendientes"                             # Si no hay tareas pendientes, devolvemos un mensaje indicando eso

sistema_tareas = SistemaGestionTareas()                               # Creamos una instancia del sistema de gestión de tareas

sistema_tareas.agregar_tarea("Hacer la compra")
sistema_tareas.agregar_tarea("Estudiar para el examen")               # Agregamos algunas tareas
sistema_tareas.agregar_tarea("Enviar el informe")

sistema_tareas.marcar_completada(1)                                   # Marcamos la segunda tarea como completada

proxima_tarea = sistema_tareas.proxima_tarea_pendiente()              # Mostramos la próxima tarea pendiente
print("Próxima tarea pendiente:", proxima_tarea)



"""
LA IMPRESIÓN FINAL SERÁ:

Próxima tarea pendiente: Hacer la compra

"""