"""Punto de entrada del ejemplo de análisis de ventas."""

from ventas import analizar_ventas, cargar_ventas


DATOS_EJEMPLO = [
    {"producto": "Café", "categoria": "Bebidas", "cantidad": 10, "precio": 2.50},
    {"producto": "Té", "categoria": "Bebidas", "cantidad": 8, "precio": 1.75},
    {"producto": "Pan", "categoria": "Alimentos", "cantidad": 12, "precio": 1.25},
    {"producto": "Queso", "categoria": "Alimentos", "cantidad": 4, "precio": 4.50},
]


def main():
    """Carga un CSV indicado como argumento o utiliza los datos de ejemplo."""
    import sys

    try:
        ventas = cargar_ventas(sys.argv[1]) if len(sys.argv) > 1 else DATOS_EJEMPLO
        if not ventas:
            print("No hay ventas válidas para analizar.")
            return

        resumen = analizar_ventas(ventas)
        print("=== Resumen de ventas ===")
        print(f"Registros de productos: {resumen['cantidad_productos']}")
        print(f"Unidades vendidas: {resumen['total_unidades']}")
        print(f"Ingresos totales: ${resumen['total_ingresos']:.2f}")
        print(f"Promedio de ingresos por producto: ${resumen['promedio_por_producto']:.2f}")
        print("Ingresos por categoría:")
        for categoria, total in resumen["ingresos_por_categoria"].items():
            print(f"  - {categoria}: ${total:.2f}")
    except (OSError, ValueError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
