class TaskManager:
    def __init__(self):
        self.tasks = []  # Inicializa una lista vacía para almacenar las tareas.

    def add_task(self, task):
        if task:  # Verifica que la tarea no esté vacía.
            self.tasks.append(task)  # Añade la tarea a la lista.

    def edit_task(self, index, task):
        # Verifica que el índice esté dentro del rango y que la nueva tarea no esté vacía.
        if 0 <= index < len(self.tasks) and task:
            self.tasks[index] = task  # Reemplaza la tarea en el índice especificado.

    def delete_task(self, index):
        # Verifica que el índice esté dentro del rango.
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)  # Elimina la tarea en el índice especificado.

    def complete_task(self, index):
        # Verifica que el índice esté dentro del rango.
        if 0 <= index < len(self.tasks):
            self.tasks[index] += " (Completada)"  # Marca la tarea como completada.

    def get_tasks(self):
        return self.tasks  # Devuelve la lista de tareas.