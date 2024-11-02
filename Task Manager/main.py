from tkinter import Tk
from src.views.views import views  # Importa la clase views

root = Tk()
app = views(root)  # Crea una instancia de TaskManagerGUI, pasando la ventana principal 'root' como argumento para que la GUI se vincule a esta ventana.
root.mainloop()
