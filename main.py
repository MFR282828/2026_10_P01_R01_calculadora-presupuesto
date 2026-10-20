# ==============================================================================
# SAGA DE REPOSITORIOS PYTHON 2026
# Repositorio: 2026_10_P01_R01_calculadora-presupuesto
# Principio 1: Fundamentos del lenguaje Python (Nivel Básico)
# ==============================================================================

# --- ENTRADA DE DATOS ---
print("========================================")
print("     CALCULADORA DE PRESUPUESTO        ")
print("========================================")

nombre_cliente = input ("Ingrese el nombre del cliente: ")
nombre_producto = input("Ingrese el nombre del producto: ")

entrada_precio = input("Ingrese el precio unitario: ")
precio_unitario = float(entrada_precio)

entrada_cantidad = input("Ingrese la cantidad de unidades: ")
cantidad = int(entrada_cantidad)

entrada_descuento = input("Ingrese el porcentaje de descuento (0 a 100): ")
porcentaje_descuento = float(entrada_descuento)

# --- CÁLCULOS Y OPERACIONES ARITMÉTICAS ---
subtotal = precio_unitario * cantidad
importe_descuento = subtotal * (porcentaje_descuento / 100.0)
total_final = subtotal - importe_descuento

# --- SALIDA DE RESULTADOS ---
print("\n========================================")
print("          RESUMEN DE COMPRA             ")
print("========================================")
print("Cliente:", nombre_cliente)
print("Producto:", nombre_producto)
print("Precio unitario:", precio_unitario)
print("Cantidad comprada:", cantidad)
print("----------------------------------------")
print("Subtotal:", subtotal)
print("Descuento aplicado:", porcentaje_descuento, "%")
print("Importe descontado:", importe_descuento)
print("----------------------------------------")
print("TOTAL FINAL A PAGAR:", total_final)
print("========================================")