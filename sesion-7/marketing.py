# 1. Importar librerías necesarias
import pandas as pd
from sklearn.linear_model import LinearRegression

# 2. Leer archivo CSV
data = pd.read_csv('marketing.csv')

x = data[['marketing']] # ahora, para evitar el error de forma de entrada, se selecciona la columna 'marketing' como un DataFrame en lugar de una Serie
print(f"{x}")

y = data['ventas']
print(f"{y}")

# 3. Creamos y entrenamos el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(x, y)

# 4. Hacer predicciones
# prediccion = modelo.predict([[6]]) # antes
column = pd.DataFrame([[9]], columns=['marketing'])
prediccion = modelo.predict(column) # ahora, para evitar el error de forma de entrada, se crea un DataFrame con la misma estructura que el conjunto de datos original

# 5. Imprimir el resultado
print(f"La predicción de ventas para una inversión de $9000 en marketing es: {prediccion[0]*1000}")