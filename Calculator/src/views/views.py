from tkinter import Entry, Button, messagebox, StringVar, SINGLE, END
from src.controllers.logic import calculate_advanced

class views:
    def __init__(self, root):
        # Inicializa la ventana principal de la calculadora
        self.root = root
        self.root.title("Calculadora Avanzada")  # Título de la ventana
        self.root.geometry("400x600")  # Dimensiones de la ventana
        self.root.resizable(False, False)  # La ventana no se puede redimensionar
        
        self.display_text = StringVar()  # Variable para el texto de la pantalla
        self.display_text.set("")  # Inicializa la pantalla vacía
        
        # Crea la entrada para mostrar el texto
        self.display = Entry(root, textvariable=self.display_text, font=("Arial", 24), 
                             bd=0, insertwidth=2, width=14, borderwidth=5, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, pady=20, padx=10)  # Posiciona la entrada

        self.create_buttons()  # Crea los botones de la calculadora
        self.setup_grid()  # Configura la rejilla para el layout

    def create_buttons(self):
        # Define los botones numéricos y de operaciones básicas
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)]
        
        # Crea botones para cada entrada
        for (text, row, col) in buttons:
            if not text == '=':
                button = Button(self.root, text=text, command=lambda t=text: self.update_display(t))
            else:
                button = Button(self.root, text=text, command=self.calculate, bg="#f08a5d")
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")  # Posiciona los botones

        # Define los botones para operaciones avanzadas
        advanced_operations = [
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2),
            ('√', 6, 0), ('log', 6, 1), ('C', 6, 2)]

        # Crea botones para operaciones avanzadas
        for (text, row, col) in advanced_operations:
            if text == 'C':
                button = Button(self.root, text=text, command=self.clear_display, bg="#f08a5d")
            else:
                button = Button(self.root, text=text, command=lambda t=text: calculate_advanced(t, self.display_text))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")  # Posiciona los botones

    def update_display(self, value):
        # Actualiza la pantalla con el valor seleccionado
        self.display_text.set(self.display_text.get() + str(value))

    def calculate(self):
        # Intenta evaluar la expresión matemática ingresada
        try:
            expression = self.display_text.get()
            self.display_text.set(eval(expression))  # Evalúa la expresión y muestra el resultado

        except Exception:
            messagebox.showerror("Error", "Entrada inválida")  # Maneja errores de entrada
            self.display_text.set("")  # Limpia la pantalla en caso de error

    def clear_display(self):
        # Limpia la pantalla
        self.display_text.set("")

    def setup_grid(self):
        # Configura las filas y columnas de la rejilla para que se expandan
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)

        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)