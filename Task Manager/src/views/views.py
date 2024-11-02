from tkinter import Button, Listbox, messagebox, simpledialog, SINGLE, END
from src.controllers.logic import TaskManager

class TaskManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("420x425")
        self.root.resizable(False, False)

        self.task_manager = TaskManager()

        self.task_listbox = Listbox(root, selectmode=SINGLE, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.add_task_button = Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.edit_task_button = Button(root, text="Editar Tarea", command=self.edit_task)
        self.edit_task_button.pack(pady=5)

        self.delete_task_button = Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        self.complete_task_button = Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

    def add_task(self):
        task = simpledialog.askstring("Nueva Tarea", "Introduce la tarea:")
        self.task_manager.add_task(task)
        self.update_task_list()

    def edit_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = simpledialog.askstring("Editar Tarea", "Modifica la tarea:", initialvalue=self.task_manager.get_tasks()[selected_index])
            self.task_manager.edit_task(selected_index, task)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para editar.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_manager.delete_task(selected_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_manager.complete_task(selected_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def update_task_list(self):
        self.task_listbox.delete(0, END)
        for task in self.task_manager.get_tasks():
            self.task_listbox.insert(END, task)