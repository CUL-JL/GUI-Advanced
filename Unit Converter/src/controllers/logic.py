def convertir_longitud(valor, unidad_origen, unidad_destino):
    # Definimos un diccionario que mapea las unidades de longitud a su valor en metros.
    unidades = {
        'metros': 1,
        'kilómetros': 1000,
        'centímetros': 0.01,
        'milímetros': 0.001,
        'pulgadas': 0.0254,
        'pies': 0.3048
    }
    
    # Realizamos la conversión multiplicando el valor original por el factor de conversiónde la unidad destino sobre la unidad de origen.
    return valor * (unidades[unidad_destino] / unidades[unidad_origen])

def convertir_peso(valor, unidad_origen, unidad_destino):
    # Similar a la función de longitud, definimos un diccionario para las unidades de peso.
    unidades = {
        'kilogramos': 1,
        'gramos': 0.001,
        'libras': 0.453592,
        'onzas': 0.0283495
    }
    # Convertimos el valor usando el mismo método de factores de conversión.
    return valor * (unidades[unidad_destino] / unidades[unidad_origen])

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    # Esta función maneja conversiones entre Celsius, Fahrenheit y Kelvin.
    if unidad_origen == 'Celsius':
        if unidad_destino == 'Fahrenheit':
            # Fórmula para convertir Celsius a Fahrenheit.
            return valor * 9/5 + 32
        elif unidad_destino == 'Kelvin':
            # Conversión de Celsius a Kelvin.
            return valor + 273.15
        else:
            return valor  # Si la unidad destino es Celsius, no hay cambio.
    elif unidad_origen == 'Fahrenheit':
        if unidad_destino == 'Celsius':
            # Conversión de Fahrenheit a Celsius.
            return (valor - 32) * 5/9
        elif unidad_destino == 'Kelvin':
            # Conversión de Fahrenheit a Kelvin.
            return (valor - 32) * 5/9 + 273.15
        else:
            return valor  # Sin cambio si la unidad destino es Fahrenheit.
    elif unidad_origen == 'Kelvin':
        if unidad_destino == 'Celsius':
            # Conversión de Kelvin a Celsius.
            return valor - 273.15
        elif unidad_destino == 'Fahrenheit':
            # Conversión de Kelvin a Fahrenheit.
            return (valor - 273.15) * 9/5 + 32
        else:
            return valor  # Sin cambio si la unidad destino es Kelvin.