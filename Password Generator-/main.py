import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        self.tasks = []

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.add_task_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.edit_task_button = tk.Button(root, text="Editar Tarea", command=self.edit_task)
        self.edit_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        self.complete_task_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

    def add_task(self):
        task = simpledialog.askstring("Nueva Tarea", "Introduce la tarea:")
        if task:
            self.tasks.append(task)
            self.update_task_list()

    def edit_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = simpledialog.askstring("Editar Tarea", "Modifica la tarea:", initialvalue=self.tasks[selected_index])
            if task:
                self.tasks[selected_index] = task
                self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para editar.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index] += " (Completada)"
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
