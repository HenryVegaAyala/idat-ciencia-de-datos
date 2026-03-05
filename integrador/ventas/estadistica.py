import numpy as np
import scipy.stats as st


def analisis_estadistico(datos_completos):
    print("Análisis estadístico de los datos:")

    montos = datos_completos["monto_comprado"].values
    promedio = np.mean(montos)
    intervalo = st.t.interval(0.95, df=len(montos) - 1, loc=np.mean(montos), scale=st.sem(montos))

    print(f"El ticket promedio de compra es: ${promedio:.2f}")
    print(f"Estamos 95% seguros de que el promedio real de TODOS los clientes está entre: ${intervalo[0]:.2f} y ${intervalo[1]:.2f}")

    # Prueba T: ¿los jóvenes (<35) gastan distinto que los mayores?
    jovenes = datos_completos[datos_completos["edad"] < 35]["monto_comprado"]
    mayores = datos_completos[datos_completos["edad"] >= 35]["monto_comprado"]

    resultado = st.ttest_ind(jovenes, mayores)
    p_valor = resultado.pvalue

    if p_valor < 0.05:
        print("Conclusión estadística: Sí, está comprobado científicamente que los jóvenes gastan distinto.\n")
    else:
        print("Conclusión estadística: La diferencia de gastos podría ser por simple casualidad.\n")