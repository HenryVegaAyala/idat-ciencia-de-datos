import pandas as pd

cliente = pd.read_csv('clientes.csv')
vendas = pd.read_csv('facturacion.csv')

# Merge de los DataFrames utilizando la columna 'id_cliente' como clave
df_merged = pd.merge(cliente, vendas, on='id_cliente', how='inner')

print(df_merged)