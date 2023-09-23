def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando un porcentaje al monto total de la compra.

    :param monto_total: El monto total de la compra.
    :param porcentaje_descuento: El porcentaje de descuento a aplicar (por defecto, 10%).
    :return: El monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamadas a la función calcular_descuento
monto_compra1 = 100
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1

monto_compra2 = 200
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final2 = monto_compra2 - descuento2

# Salida de resultados
print(f"Compra 1: Monto Total = ${monto_compra1}, Descuento = ${descuento1}, Monto Final = ${monto_final1}")
print(f"Compra 2: Monto Total = ${monto_compra2}, Descuento = ${descuento2}, Monto Final = ${monto_final2}")
