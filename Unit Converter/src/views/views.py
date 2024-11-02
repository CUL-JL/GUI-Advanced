from tkinter import Tk, Label, Entry, Button, ttk, messagebox
from src.controllers.logic import convertir_longitud, convertir_peso, convertir_temperatura

class views:
    def __init__(self, root):
        # Inicializa la ventana principal con título y tamaño fijo
        self.root = root
        self.root.title("Conversor de Unidades")
        self.root.geometry("195x250")
        self.root.resizable(False, False)

        # Entrada de valor a convertir
        self.entry_value = Entry(root)
        self.entry_value.grid(row=0, column=1, padx=10, pady=10)

        # ComboBox para seleccionar el tipo de unidad (Longitud, Peso, Temperatura)
        self.combo_tipo_unidad = ttk.Combobox(root, values=["Longitud", "Peso", "Temperatura"])
        self.combo_tipo_unidad.grid(row=1, column=1, padx=10, pady=10)
        self.combo_tipo_unidad.bind("<<ComboboxSelected>>", self.actualizar_unidades)  # Llama a actualizar_unidades al seleccionar
        self.combo_tipo_unidad.current(0)  # Establece Longitud como opción por defecto

        # ComboBox para seleccionar la unidad de origen
        self.combo_unidad_origen = ttk.Combobox(root)
        self.combo_unidad_origen.grid(row=2, column=1, padx=10, pady=10)

        # ComboBox para seleccionar la unidad de destino
        self.combo_unidad_destino = ttk.Combobox(root)
        self.combo_unidad_destino.grid(row=3, column=1, padx=10, pady=10)

        # Botón para realizar la conversión
        btn_convertir = Button(root, text="Convertir", command=self.convertir)
        btn_convertir.grid(row=4, column=1, padx=10, pady=10)

        # Etiqueta para mostrar el resultado de la conversión
        self.label_resultado = Label(root, text="Resultado: ")
        self.label_resultado.grid(row=5, column=1, padx=10, pady=10)

        self.actualizar_unidades()  # Inicializa las unidades al inicio

    def convertir(self):
        try:
            # Obtiene el valor a convertir y las unidades seleccionadas
            valor = float(self.entry_value.get())
            tipo_unidad = self.combo_tipo_unidad.get()
            unidad_origen = self.combo_unidad_origen.get()
            unidad_destino = self.combo_unidad_destino.get()
            
            # Realiza la conversión según el tipo de unidad seleccionado
            if tipo_unidad == 'Longitud':
                resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
            elif tipo_unidad == 'Peso':
                resultado = convertir_peso(valor, unidad_origen, unidad_destino)
            elif tipo_unidad == 'Temperatura':
                resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
            
            # Muestra el resultado en la etiqueta
            self.label_resultado.config(text=f"Resultado: {resultado:.2f} {unidad_destino}")
        except ValueError:
            # Manejo de errores para entradas no válidas
            messagebox.showerror("Error", "Por favor ingrese un número válido.")

    def actualizar_unidades(self, event=None):
        # Actualiza las unidades en los ComboBox según el tipo de unidad seleccionado
        tipo_unidad = self.combo_tipo_unidad.get()
        if tipo_unidad == 'Longitud':
            unidades = ['metros', 'kilómetros', 'centímetros', 'milímetros', 'pulgadas', 'pies']
        elif tipo_unidad == 'Peso':
            unidades = ['kilogramos', 'gramos', 'libras', 'onzas']
        elif tipo_unidad == 'Temperatura':
            unidades = ['Celsius', 'Fahrenheit', 'Kelvin']
        
        # Establece las unidades disponibles en los ComboBox de origen y destino
        self.combo_unidad_origen['values'] = unidades
        self.combo_unidad_destino['values'] = unidades
        self.combo_unidad_origen.current(0)  # Establece la primera unidad como predeterminada
        self.combo_unidad_destino.current(0)  # Lo mismo para la unidad de destino