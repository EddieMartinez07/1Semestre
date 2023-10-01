# Crear el diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Eddie Roberto",
    "edad": 30,
    "ciudad": "Ciudad A",
    "profesion": "Ingeniero"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor para la "profesion"
informacion_personal["profesion"] = "Doctor"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "09965345123"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario actualizado
print(informacion_personal)
