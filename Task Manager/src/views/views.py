from tkinter import Button, Listbox, messagebox, simpledialog, SINGLE, END
from src.controllers.logic import TaskManager

class views:
    def __init__(self, root):
        # Inicializa la ventana principal de la aplicación
        self.root = root
        self.root.title("Gestor de Tareas")  # Establece el título de la ventana
        self.root.geometry("420x425")  # Establece el tamaño de la ventana
        self.root.resizable(False, False)  # Hace que la ventana no sea redimensionable

        # Crea una instancia del gestor de tareas
        self.task_manager = TaskManager()

        # Configura la lista de tareas
        self.task_listbox = Listbox(root, selectmode=SINGLE, width=50, height=15)  # Crea un Listbox para mostrar tareas
        self.task_listbox.pack(pady=10)  # Añade el Listbox a la ventana

        # Botón para añadir una nueva tarea
        self.add_task_button = Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)  # Añade el botón a la ventana

        # Botón para editar la tarea seleccionada
        self.edit_task_button = Button(root, text="Editar Tarea", command=self.edit_task)
        self.edit_task_button.pack(pady=5)  # Añade el botón a la ventana

        # Botón para eliminar la tarea seleccionada
        self.delete_task_button = Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)  # Añade el botón a la ventana

        # Botón para marcar la tarea seleccionada como completada
        self.complete_task_button = Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)  # Añade el botón a la ventana

    def add_task(self):
        # Solicita al usuario que introduzca una nueva tarea
        task = simpledialog.askstring("Nueva Tarea", "Introduce la tarea:")
        self.task_manager.add_task(task)  # Añade la tarea al gestor
        self.update_task_list()  # Actualiza la lista de tareas mostradas

    def edit_task(self):
        try:
            # Intenta obtener la tarea seleccionada
            selected_index = self.task_listbox.curselection()[0]
            # Solicita al usuario que modifique la tarea
            task = simpledialog.askstring("Editar Tarea", "Modifica la tarea:", initialvalue=self.task_manager.get_tasks()[selected_index])
            self.task_manager.edit_task(selected_index, task)  # Edita la tarea en el gestor
            self.update_task_list()  # Actualiza la lista de tareas mostradas
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para editar.")  # Muestra advertencia si no hay tarea seleccionada

    def delete_task(self):
        try:
            # Intenta obtener la tarea seleccionada
            selected_index = self.task_listbox.curselection()[0]
            self.task_manager.delete_task(selected_index)  # Elimina la tarea en el gestor
            self.update_task_list()  # Actualiza la lista de tareas mostradas
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")  # Muestra advertencia si no hay tarea seleccionada

    def complete_task(self):
        try:
            # Intenta obtener la tarea seleccionada
            selected_index = self.task_listbox.curselection()[0]
            self.task_manager.complete_task(selected_index)  # Marca la tarea como completada en el gestor
            self.update_task_list()  # Actualiza la lista de tareas mostradas
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")  # Muestra advertencia si no hay tarea seleccionada

    def update_task_list(self):
        # Limpia la lista actual y la vuelve a llenar con las tareas del gestor
        self.task_listbox.delete(0, END)  # Borra todos los elementos de la lista
        for task in self.task_manager.get_tasks():
            self.task_listbox.insert(END, task)  # Inserta cada tarea en el Listbox