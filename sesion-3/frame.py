import pandas as pd

datos = {
    'Nombre': ['Ana', 'Luis'],
    'Edad': [28, 34],
}
resultado = pd.DataFrame(datos)
# print(resultado)

serie = pd.Series([100, 200, 150, 300])
print(serie)