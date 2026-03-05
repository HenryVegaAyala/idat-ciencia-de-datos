from sklearn.linear_model import LinearRegression
import pandas as pd

def modelos_predictivos(datos_completos):

    df = datos_completos.copy()
    x_reg  = df[["edad", "visitas_web"]]
    y_clas = df["compro_premium"]

    # A. Regresión Lineal: estima cuánto gastará un cliente
    regresion = LinearRegression()
    regresion.fit(x_reg, y_clas)

    consulta = pd.DataFrame([[30, 10]], columns=["edad", "visitas_web"])
    prediccion = regresion.predict(consulta)

    print(f"[Regresion Lineal] Un cliente de 30 años con 10 visitas gastará aprox: ${prediccion[0]:.2f}")
