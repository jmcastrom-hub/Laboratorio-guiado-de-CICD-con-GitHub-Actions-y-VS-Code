def calcular_total(precio, cantidad):
    """Calcula el total de una venta y rechaza precios negativos."""
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    return precio * cantidad


def aplicar_descuento(total, porcentaje):
    """Aplica al total un descuento expresado como porcentaje."""
    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100.")
    return total * (1 - porcentaje / 100)
