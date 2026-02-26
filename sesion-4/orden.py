import pandas as pd

data = pd.read_csv("ventas_enero.csv")

# orden = data.sort_values("cantidad", ascending=False)

# print(orden)

# data["total"] = data["cantidad"] * data["precio_unitario"]
# print(data)

# Agregar nuevas filas al DataFrame
nueva_fila = {
    "id_venta": 1000,
    "producto": "Producto D",
    "cantidad": 15,
    "precio_unitario": 12.5,
    "vendedor": "Pepito"
}

resultado_nueva_fila = pd.DataFrame([nueva_fila])

resultado_concatenado = pd.concat([data, resultado_nueva_fila], ignore_index=True)

resultado_concatenado["total"] = resultado_concatenado["cantidad"] * resultado_concatenado["precio_unitario"]

resultado_concatenado.rename(columns={"total": "total_venta"}, inplace=True)

print(resultado_concatenado.sort_values("id_venta", ascending=True))

