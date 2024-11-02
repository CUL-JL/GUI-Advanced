from tkinter import Tk, Label, Entry, Button, ttk, messagebox
from src.controllers.logic import convertir_longitud, convertir_peso, convertir_temperatura

def convertir():
    try:
        valor = float(entry_value.get())
        tipo_unidad = combo_tipo_unidad.get()
        unidad_origen = combo_unidad_origen.get()
        unidad_destino = combo_unidad_destino.get()
        
        if tipo_unidad == 'Longitud':
            resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
        elif tipo_unidad == 'Peso':
            resultado = convertir_peso(valor, unidad_origen, unidad_destino)
        elif tipo_unidad == 'Temperatura':
            resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
        
        label_resultado.config(text=f"Resultado: {resultado:.2f} {unidad_destino}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido.")

def actualizar_unidades():
    tipo_unidad = combo_tipo_unidad.get()
    if tipo_unidad == 'Longitud':
        unidades = ['metros', 'kilómetros', 'centímetros', 'milímetros', 'pulgadas', 'pies']
    elif tipo_unidad == 'Peso':
        unidades = ['kilogramos', 'gramos', 'libras', 'onzas']
    elif tipo_unidad == 'Temperatura':
        unidades = ['Celsius', 'Fahrenheit', 'Kelvin']
    
    combo_unidad_origen['values'] = unidades
    combo_unidad_destino['values'] = unidades
    combo_unidad_origen.current(0)
    combo_unidad_destino.current(0)

# Configuración de la root
root = Tk()
root.title("Conversor de Unidades")
root.geometry("195x250")
root.resizable(False, False)

# Entradas
entry_value = Entry(root)
entry_value.grid(row=0, column=1, padx=10, pady=10)

# Tipo de unidad
combo_tipo_unidad = ttk.Combobox(root, values=["Longitud", "Peso", "Temperatura"])
combo_tipo_unidad.grid(row=1, column=1, padx=10, pady=10)
combo_tipo_unidad.bind("<<ComboboxSelected>>", lambda e: actualizar_unidades())
combo_tipo_unidad.current(0)

# Unidades
combo_unidad_origen = ttk.Combobox(root)
combo_unidad_origen.grid(row=2, column=1, padx=10, pady=10)

combo_unidad_destino = ttk.Combobox(root)
combo_unidad_destino.grid(row=3, column=1, padx=10, pady=10)

# Botón de conversión
btn_convertir = Button(root, text="Convertir", command=convertir)
btn_convertir.grid(row=4, column=1, padx=10, pady=10)

# Resultado
label_resultado = Label(root, text="Resultado: ")
label_resultado.grid(row=5, column=1, padx=10, pady=10)

actualizar_unidades()  # Inicializa las unidades al inicio
root.mainloop()