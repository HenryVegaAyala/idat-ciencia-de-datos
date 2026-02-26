import pandas as pd
from httplib2.iri2uri import escape_range

ventas = pd.read_csv("ventas_enero.csv")

ventas_grandes = ventas[ventas["cantidad"] >= 5]

# print(ventas_grandes)

#Filtros avanzados

# ventas_por_precio = ventas[(ventas["cantidad"] >= 2) & (ventas["precio_unitario"] >= 50)]
# print(ventas_por_precio)

# ventas_por_precio = ventas[(ventas["cantidad"] >= 2) | (ventas["precio_unitario"] >= 50)]
# print(ventas_por_precio)

ventas_por_precio = ventas[(ventas["cantidad"] == 2)]
# print(ventas_por_precio)

# Igual es
a = 2

# Comparativa es
# a = 2
# esigual = a == 31
# print(f"Es igual a 31? {esigual}")

vendedor_ana = ventas[ventas["vendedor"] == "Ana"]
print(vendedor_ana)

