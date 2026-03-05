# 1. Importar librerías necesarias
import pandas as pd
from sklearn.linear_model import LinearRegression

# 2. Leer archivo CSV
data = pd.read_csv('marketing.csv')

# ahora, para evitar el error de forma de entrada, se selecciona la columna Ej 'marketing' como un DataFrame en lugar de una Serie
x = data[['marketing']]
print(f"-"*60)
print(f"{x}")
print(f"-"*60)

# ahora se selecciona la columna 'ventas' como una Serie
y = data['ventas']
print(f"*"*60)
print(f"{y}")
print(f"*"*60)

# 3. Creamos y entrenamos el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(x, y) # se entrena el modelo con los datos de marketing (x) y ventas (y)

# 4. Hacer predicciones

# Crearmos un nuevo registro para la predicción.
column = pd.DataFrame([[6000]], columns=['marketing'])
print(f"Columna de entrada para predicción:\n{column}")
prediccion = modelo.predict(column) # ahora, para evitar el error de forma de entrada, se crea un DataFrame con la misma estructura que el conjunto de datos original

# 5. Imprimir el resultado
print(f"La predicción de ventas para una inversión de $6000 en marketing es: {prediccion[0]}")

# Otra predicción con un nuevo valor
column = pd.DataFrame([[10000]], columns=['marketing'])
prediccion = modelo.predict(column)
print(f"La predicción de ventas para una inversión de $10000 en marketing es: {prediccion[0]}")