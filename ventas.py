"""Funciones básicas para cargar y analizar datos de ventas."""

import csv
from collections import defaultdict
from pathlib import Path


def cargar_ventas(ruta):
    """Carga ventas desde un CSV con columnas producto, categoria, cantidad y precio.

    Devuelve una lista de diccionarios. Las filas con datos faltantes o
    valores numéricos inválidos se omiten; los errores de archivo se informan.
    """
    ventas = []
    try:
        with Path(ruta).open("r", encoding="utf-8-sig", newline="") as archivo:
            lector = csv.DictReader(archivo)
            requeridas = {"producto", "categoria", "cantidad", "precio"}
            if not lector.fieldnames or not requeridas.issubset(lector.fieldnames):
                raise ValueError(
                    "El CSV debe incluir las columnas: producto, categoria, cantidad y precio."
                )

            for numero, fila in enumerate(lector, start=2):
                try:
                    producto = (fila["producto"] or "").strip()
                    categoria = (fila["categoria"] or "").strip()
                    cantidad = int(fila["cantidad"])
                    precio = float(fila["precio"])
                    if not producto or not categoria or cantidad < 0 or precio < 0:
                        raise ValueError("campos vacíos o valores negativos")
                    ventas.append({
                        "producto": producto,
                        "categoria": categoria,
                        "cantidad": cantidad,
                        "precio": precio,
                    })
                except (TypeError, ValueError):
                    print(f"Aviso: se omite la fila {numero} por datos inválidos.")
    except OSError as error:
        raise OSError(f"No se pudo leer el archivo '{ruta}': {error}") from error
    return ventas


def analizar_ventas(ventas):
    """Calcula ingresos, unidades, promedio por producto y resumen por categoría."""
    ingresos_por_categoria = defaultdict(float)
    total_ingresos = 0.0
    total_unidades = 0

    for venta in ventas:
        subtotal = venta["cantidad"] * venta["precio"]
        total_ingresos += subtotal
        total_unidades += venta["cantidad"]
        ingresos_por_categoria[venta["categoria"]] += subtotal

    return {
        "total_ingresos": total_ingresos,
        "total_unidades": total_unidades,
        "promedio_por_producto": total_ingresos / len(ventas) if ventas else 0.0,
        "ingresos_por_categoria": dict(sorted(ingresos_por_categoria.items())),
        "cantidad_productos": len(ventas),
    }
