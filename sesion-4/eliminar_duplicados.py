import pandas as pd

df = pd.read_csv('ventas.csv')

print(f"Data original")
print(df)

# Eliminar filas duplicadas
print(f"+" * 90)
print(f"Data duplicada eliminada")
df_sin_duplicados = df.drop_duplicates()
print(df_sin_duplicados)

print("+" * 90)
print(f"Data guarda en un nuevo archivo CSV")
df_sin_duplicados.to_csv('ventas_corregidas.csv', index=False)