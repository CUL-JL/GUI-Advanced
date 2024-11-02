def convertir_longitud(valor, unidad_origen, unidad_destino):
    unidades = {
        'metros': 1,
        'kilómetros': 1000,
        'centímetros': 0.01,
        'milímetros': 0.001,
        'pulgadas': 0.0254,
        'pies': 0.3048
    }
    return valor * (unidades[unidad_destino] / unidades[unidad_origen])

def convertir_peso(valor, unidad_origen, unidad_destino):
    unidades = {
        'kilogramos': 1,
        'gramos': 0.001,
        'libras': 0.453592,
        'onzas': 0.0283495
    }
    return valor * (unidades[unidad_destino] / unidades[unidad_origen])

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == 'Celsius':
        if unidad_destino == 'Fahrenheit':
            return valor * 9/5 + 32
        elif unidad_destino == 'Kelvin':
            return valor + 273.15
        else:
            return valor
    elif unidad_origen == 'Fahrenheit':
        if unidad_destino == 'Celsius':
            return (valor - 32) * 5/9
        elif unidad_destino == 'Kelvin':
            return (valor - 32) * 5/9 + 273.15
        else:
            return valor
    elif unidad_origen == 'Kelvin':
        if unidad_destino == 'Celsius':
            return valor - 273.15
        elif unidad_destino == 'Fahrenheit':
            return (valor - 273.15) * 9/5 + 32
        else:
            return valor
