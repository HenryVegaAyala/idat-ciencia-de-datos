import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("dato_credito.csv")

x = df[["ingreso", "morosidad"]]
y = df["aprobado"]

arbol = DecisionTreeClassifier()
arbol.fit(x, y)

ingresos_netos = 8000
tienes_morosidad = 1

respuestaData = pd.DataFrame([[ingresos_netos, tienes_morosidad]], columns=["ingreso", "morosidad"])
respuesta = arbol.predict(respuestaData)

if respuesta[0] == 1:
    print("El crédito ha sido aprobado.")
else:
    print("El crédito ha sido rechazado.")
