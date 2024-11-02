import math
from tkinter import messagebox

def calculate_advanced(operation, display_text):
    try:
        value = float(display_text.get())
        
        match operation:
            case "sin":
                result = math.sin(math.radians(value))
            case "cos":
                result = math.cos(math.radians(value))
            case "tan":
                result = math.tan(math.radians(value))
            case "√":
                result = math.sqrt(value)
            case "log":
                result = math.log10(value)
            case _:
                raise ValueError("Operación no válida")
        
        display_text.set(result)

    except ValueError as e:
        messagebox.showerror("Error", str(e))
        display_text.set("")
        
    except Exception:
        messagebox.showerror("Error", "Error desconocido")
        display_text.set("")
