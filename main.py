from ventas import aplicar_descuento, calcular_total


producto = "Laptop"
precio = 450000
cantidad = 2
subtotal = calcular_total(precio, cantidad)
porcentaje_descuento = 10
total = aplicar_descuento(subtotal, porcentaje_descuento)

print(f"Producto: {producto}")
print(f"Precio por unidad: {precio}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: {subtotal}")
print(f"Descuento: {porcentaje_descuento} %")
print(f"Total final: {total:.0f}")
