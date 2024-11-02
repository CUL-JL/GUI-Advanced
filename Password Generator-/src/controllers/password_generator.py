import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ''

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_lowercase:
        characters += string.ascii_lowercase

    if use_digits:
        characters += string.digits
        
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("Debe seleccionar al menos un tipo de carácter.")

    return ''.join(random.choice(characters) for _ in range(length))
