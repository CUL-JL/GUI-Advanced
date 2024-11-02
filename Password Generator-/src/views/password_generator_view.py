from tkinter import Frame, Label, LabelFrame, Spinbox, Checkbutton, messagebox, Button, BooleanVar, IntVar
from src.controllers.password_generator import generate_password

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Contraseñas Avanzado")
        self.root.geometry("400x360")
        self.root.resizable(False, False)
        
        # Variables
        self.password_length = IntVar(value=12)
        self.include_uppercase = BooleanVar(value=True)
        self.include_lowercase = BooleanVar(value=True)
        self.include_digits = BooleanVar(value=True)
        self.include_special = BooleanVar(value=True)
        
        # Título
        title_label = Label(root, text="Generador de Contraseñas", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)
        
        # Controles de longitud
        length_frame = Frame(root)
        length_frame.pack(pady=5)
        length_label = Label(length_frame, text="Longitud de la contraseña:")
        length_label.pack(side="left")
        length_spinbox = Spinbox(length_frame, from_=6, to=32, textvariable=self.password_length, width=5)
        length_spinbox.pack(side="left", padx=5)

        # Opciones de caracteres
        options_frame = LabelFrame(root, text="Incluir:")
        options_frame.pack(pady=10, fill="x", padx=10)
        
        uppercase_check = Checkbutton(options_frame, text="Mayúsculas", variable=self.include_uppercase)
        uppercase_check.pack(anchor="w")
        lowercase_check = Checkbutton(options_frame, text="Minúsculas", variable=self.include_lowercase)
        lowercase_check.pack(anchor="w")
        digits_check = Checkbutton(options_frame, text="Números", variable=self.include_digits)
        digits_check.pack(anchor="w")
        special_check = Checkbutton(options_frame, text="Caracteres Especiales", variable=self.include_special)
        special_check.pack(anchor="w")
        
        # Botón para generar contraseña
        generate_button = Button(root, text="Generar Contraseña", command=self.generate_password)
        generate_button.pack(pady=10)
        
        # Label para mostrar la contraseña generada
        self.password_label = Label(root, text="", font=("Helvetica", 12))
        self.password_label.pack(pady=10, fill="x", padx=20)

        # Botón para copiar
        copy_button = Button(root, text="Copiar", command=self.copy_to_clipboard)
        copy_button.pack(pady=5)

    def generate_password(self):
        try:
            password = generate_password(
                length=self.password_length.get(),
                use_uppercase=self.include_uppercase.get(),
                use_lowercase=self.include_lowercase.get(),
                use_digits=self.include_digits.get(),
                use_special=self.include_special.get()
            )
            self.password_label.config(text=password)
        except ValueError as e:
            messagebox.showwarning("Advertencia", str(e))

    def copy_to_clipboard(self):
        # Verifica si el Label de la contraseña está vacío
        if not self.password_label.cget("text"):
            messagebox.showerror("Error", "Primero debe generar una contraseña.")
            return
        
        self.root.clipboard_clear()
        self.root.clipboard_append(self.password_label.cget("text"))
        messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles.")