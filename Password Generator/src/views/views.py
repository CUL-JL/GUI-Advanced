from tkinter import Frame, Label, LabelFrame, Spinbox, Checkbutton, messagebox, Button, BooleanVar, IntVar
from src.controllers.logic import generate_password

class views:
    def __init__(self, root):
        # Inicializa la ventana principal de la aplicación
        self.root = root
        self.root.title("Generador de Contraseñas Avanzado")
        self.root.geometry("400x360")  # Establece el tamaño de la ventana
        self.root.resizable(False, False)  # Desactiva el redimensionamiento de la ventana
        
        # Variables para configurar la generación de contraseñas
        self.password_length = IntVar(value=12)  # Longitud de la contraseña, valor por defecto 12
        self.include_uppercase = BooleanVar(value=True)  # Incluir mayúsculas por defecto
        self.include_lowercase = BooleanVar(value=True)  # Incluir minúsculas por defecto
        self.include_digits = BooleanVar(value=True)  # Incluir dígitos por defecto
        self.include_special = BooleanVar(value=True)  # Incluir caracteres especiales por defecto
        
        # Etiqueta de título
        title_label = Label(root, text="Generador de Contraseñas", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)  # Añade espacio vertical

        # Controles para seleccionar la longitud de la contraseña
        length_frame = Frame(root)
        length_frame.pack(pady=5)
        length_label = Label(length_frame, text="Longitud de la contraseña:")
        length_label.pack(side="left")
        length_spinbox = Spinbox(length_frame, from_=6, to=32, textvariable=self.password_length, width=5)
        length_spinbox.pack(side="left", padx=5)  # Añade espacio horizontal

        # Opciones para incluir diferentes tipos de caracteres
        options_frame = LabelFrame(root, text="Incluir:")
        options_frame.pack(pady=10, fill="x", padx=10)
        
        # Casillas de verificación para seleccionar tipos de caracteres
        uppercase_check = Checkbutton(options_frame, text="Mayúsculas", variable=self.include_uppercase)
        uppercase_check.pack(anchor="w")  # Alinear a la izquierda
        lowercase_check = Checkbutton(options_frame, text="Minúsculas", variable=self.include_lowercase)
        lowercase_check.pack(anchor="w")
        digits_check = Checkbutton(options_frame, text="Números", variable=self.include_digits)
        digits_check.pack(anchor="w")
        special_check = Checkbutton(options_frame, text="Caracteres Especiales", variable=self.include_special)
        special_check.pack(anchor="w")
        
        # Botón para generar la contraseña
        generate_button = Button(root, text="Generar Contraseña", command=self.generate_password)
        generate_button.pack(pady=10)
        
        # Etiqueta para mostrar la contraseña generada
        self.password_label = Label(root, text="", font=("Helvetica", 12))
        self.password_label.pack(pady=10, fill="x", padx=20)

        # Botón para copiar la contraseña al portapapeles
        copy_button = Button(root, text="Copiar", command=self.copy_to_clipboard)
        copy_button.pack(pady=5)

    def generate_password(self):
        # Método para generar la contraseña
        try:
            password = generate_password(
                length=self.password_length.get(),
                use_uppercase=self.include_uppercase.get(),
                use_lowercase=self.include_lowercase.get(),
                use_digits=self.include_digits.get(),
                use_special=self.include_special.get()
            )
            self.password_label.config(text=password)  # Muestra la contraseña generada
        except ValueError as e:
            messagebox.showwarning("Advertencia", str(e))  # Muestra advertencias si ocurre un error

    def copy_to_clipboard(self):
        # Método para copiar la contraseña generada al portapapeles
        if not self.password_label.cget("text"):  # Verifica si hay una contraseña generada
            messagebox.showerror("Error", "Primero debe generar una contraseña.")
            return
        
        self.root.clipboard_clear()  # Limpia el portapapeles
        self.root.clipboard_append(self.password_label.cget("text"))  # Añade la contraseña al portapapeles
        messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles.")  # Confirma la acción