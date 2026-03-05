import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('regresion_logistica.csv')

x = df[["antiguedad", "cuota_mensual"]]

y = df["fuga"]

modelo = LogisticRegression()
modelo.fit(x, y)

prediccionData = pd.DataFrame([[1, 30]], columns=["antiguedad", "cuota_mensual"])
prediccion = modelo.predict(prediccionData)

print(prediccion)

if prediccion[0] == 1:
    print("El cliente se va a ir (fuga)")
else:
    print("El cliente se va a quedar (no fuga)")
