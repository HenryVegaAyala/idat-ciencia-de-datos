# 1. Crear una lista de productos
vitrina = ["Pan", "Alfajor", "Aceite", "Mantequilla"]

# 2. Lista de números
ventas_horas = [10, 30, 15, 20]

# 3. Acceder al primer elemento (Indice 0)
primero = vitrina[0]

# 4. Acceder al último elemento
ultimo = vitrina[-1]

# 5. Contar cuántos elementos hay en una lista
total_productos = len(vitrina)

# 6. Agregar un producto al final de la lista
vitrina.append("Donut")
print(f"Vitrina después de agregar un producto: {vitrina}")

# 7. Cambiar un producto por otro de la lista
vitrina[2] = "Aceite de Oliva"
print(f"Vitrina después de cambiar un producto: {vitrina}")

# 8. Quitar un producto de la lista
vitrina.remove("Pan")
print(f"Vitrina después de quitar un producto: {vitrina}")

# 9. uso de del en una lista
del vitrina[0]
print(f"Vitrina después de usar del: {vitrina}")

# 10. uso de pop en una lista
ultimo_producto = vitrina.pop(1)
print(f"Vitrina después de usar pop: {vitrina}")
print(f"Producto eliminado con pop: {ultimo_producto}")

# 11. Verificar si un producto existe en la lista
existe_te = "Té" in vitrina
print(f"¿Existe Té en la vitrina? {existe_te}")

existe_donut = "Donut" in vitrina
print(f"¿Existe Donut en la vitrina? {existe_donut}")

# 12. Filtrar productos que contienen la letra ''
vitrina_filtrada = [producto for producto in vitrina if "D" in producto]
print(f"Productos que contienen la letra 'A': {vitrina_filtrada}")