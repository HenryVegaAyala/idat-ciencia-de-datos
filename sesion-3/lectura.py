import pandas as pd

resultado = pd.read_csv("ventas_enero.csv")

sub_tabla = resultado[["producto", "precio_unitario", "vendedor"]]
print(sub_tabla)