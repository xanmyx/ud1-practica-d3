"""
Calculadora de importes con descuentos para los productos de una tienda.
Descuentos: 
    - 0% de descuento para importes con precio menor a 100€.
    - 10% de descuento para importes con precio mayor o igual a 100€.  
    - 15% de descuento para importes con precio mayor o igual a 300€.
"""


def calcular_precio_final(importe):
    """Calcula el precio final aplicando el descuento correspondiente según su importe."""
    if importe <= 0:
        raise ValueError("El importe introducido no puede ser cero o negativo.")
    elif importe >= 300:
        descuento = 0.15
    elif importe >= 100:
        descuento = 0.10
    else:
        descuento = 0.0

    precio_final = importe * (1 - descuento)
    return precio_final


importe = float(input("Introduce el importe sin descuento: "))

try:
    precio_final = calcular_precio_final(importe)
    print(f"El precio final con descuento es: {precio_final:.2f}€")
except ValueError as error:
    print(f"Error: {error}")