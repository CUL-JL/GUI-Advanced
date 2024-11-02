from tkinter import Tk
from src.views.views import views  # Importa la clase views

root = Tk()
app = views(root)  # Pasándole la ventana principal al views.py
root.mainloop()