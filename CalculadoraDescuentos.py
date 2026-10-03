"""
Calculadora de precios con descuentos para los productos de una tienda.
Descuentos: 
    - 0% de descuento para productos con precio menor a 100€.
    - 10% de descuento para productos con precio mayor o igual a 100€.  
    - 15% de descuento para productos con precio mayor o igual a 300€.
"""


def calcular_precio_final(precio):
    """Calcula el precio final de un producto aplicando el descuento correspondiente según su precio."""
    if precio <= 0:
        raise ValueError("El precio introducido no puede ser cero o negativo.")
    elif precio >= 300:
        descuento = 0.15
    elif precio >= 100:
        descuento = 0.10
    else:
        descuento = 0.0

    precio_final = precio * (1 - descuento)
    return precio_final


precio = float(input("Introduce el precio sin descuento: "))

try:
    precio_final = calcular_precio_final(precio)
    print(f"El precio final con descuento es: {precio_final:.2f}€")
except ValueError as error:
    print(f"Error: {error}")