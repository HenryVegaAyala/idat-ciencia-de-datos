import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('regresion_multiple.csv')

x = df[['experiencia', 'estudios']]
y = df['salario']

modelo = LinearRegression()
modelo.fit(x, y)

# Hacemos las preguntas
prediccionData = pd.DataFrame([[4, 5]], columns=['experiencia', 'estudios'])
prediccion = modelo.predict(prediccionData)
print(f"Salario sugerido : {prediccion[0]}")

# Hacemos otra pregunta
prediccionData = pd.DataFrame([[10, 5]], columns=['experiencia', 'estudios'])
prediccion = modelo.predict(prediccionData)
print(f"Salario sugerido : {prediccion[0]}")
