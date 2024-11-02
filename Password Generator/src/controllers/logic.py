import random  # Importa el módulo random para generar números aleatorios.
import string  # Importa el módulo string, que contiene cadenas de caracteres útiles.

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    # Define una función para generar una contraseña de longitud específica.
    
    characters = ''  # Inicializa una cadena vacía para almacenar los caracteres que se usarán.

    if use_uppercase:
        # Si se permite el uso de letras mayúsculas, añade las letras mayúsculas a la lista de caracteres.
        characters += string.ascii_uppercase

    if use_lowercase:
        # Si se permite el uso de letras minúsculas, añade las letras minúsculas a la lista de caracteres.
        characters += string.ascii_lowercase

    if use_digits:
        # Si se permite el uso de dígitos, añade los números del 0 al 9 a la lista de caracteres.
        characters += string.digits
        
    if use_special:
        # Si se permite el uso de caracteres especiales, añade esos caracteres a la lista.
        characters += string.punctuation

    if not characters:
        # Si no se ha seleccionado ningún tipo de carácter, lanza una excepción.
        raise ValueError("Debe seleccionar al menos un tipo de carácter.")

    # Genera una contraseña aleatoria seleccionando caracteres al azar de la lista 'characters'.
    return ''.join(random.choice(characters) for _ in range(length))