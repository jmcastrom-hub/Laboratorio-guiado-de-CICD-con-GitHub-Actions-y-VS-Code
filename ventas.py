def calcular_total(precio, cantidad):
    """Calcula el total de una venta y rechaza precios negativos."""
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    return precio * cantidad
