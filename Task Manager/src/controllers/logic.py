class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task:
            self.tasks.append(task)

    def edit_task(self, index, task):
        if 0 <= index < len(self.tasks) and task:
            self.tasks[index] = task

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index] += " (Completada)"

    def get_tasks(self):
        return self.tasks