import json
import os

def cargar_datos():
    """Carga de manera segura el archivo data.json."""
    ruta_actual = os.path.dirname(__file__)
    ruta_json = os.path.join(ruta_actual, 'data.json')
    with open(ruta_json, 'r', encoding='utf-8') as f:
        return json.load(f)

def obtener_salario(nombre: str):
    """Busca y devuelve el salario de un empleado según su nombre."""
    datos = cargar_datos()
    nombre_limpio = nombre.strip().lower()
    if nombre_limpio in datos:
        return datos[nombre_limpio]["salario"]
    return f"Empleado '{nombre}' no encontrado en la base de datos."

def calcular_bono(salario: float, porcentaje: float):
    """Calcula el monto del bono basado en un porcentaje del salario."""
    if isinstance(salario, (int, float)):
        return salario * (porcentaje / 100)
    return "No es posible calcular el bono: el salario proporcionado no es válido."