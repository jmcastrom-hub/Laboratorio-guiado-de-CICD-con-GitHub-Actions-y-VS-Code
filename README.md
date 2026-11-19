# Análisis de ventas

Proyecto educativo en Python para cargar y analizar datos de ventas, e imprimir un resumen legible desde la terminal.

## Archivos principales

- `main.py`: ejecuta el análisis y muestra los resultados.
- `ventas.py`: contiene las funciones para cargar y analizar los datos.

## Ejecución

Desde esta carpeta, ejecuta el ejemplo integrado:

```bash
python main.py
```

El programa imprime ingresos totales, unidades vendidas, promedio de ingresos
por producto y un resumen de ingresos por categoría. También puede leer un CSV
con las columnas `producto`, `categoria`, `cantidad` y `precio`:

```bash
python main.py ventas.csv
```
