def calcular_temperatura_promedio(datos_ciudades):
    promedios_ciudades = {}

    for ciudad, temperaturas_semanales in datos_ciudades.items():
        # Calcula el promedio de temperaturas para cada ciudad
        promedio = sum(temperaturas_semanales) / len(temperaturas_semanales)
        promedios_ciudades[ciudad] = promedio

    return promedios_ciudades


# Ejemplo de uso
datos = {
    "Esmeraldas": [25, 26, 27, 24, 23],
    "Guayaquil": [30, 32, 31, 29, 28],
    "Quito": [18, 20, 19, 17, 16],
    "Manta": [28, 29, 30, 27, 26],
    "Manabí": [27, 28, 29, 26, 25],
    "Riobamba": [15, 16, 14, 15, 17]
}

resultado = calcular_temperatura_promedio(datos)

for ciudad, promedio in resultado.items():
    print(f"Temperatura promedio en {ciudad}: {promedio}°C")
