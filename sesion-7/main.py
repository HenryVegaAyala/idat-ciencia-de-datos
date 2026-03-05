import pandas as pd
import scipy.stats as st

df = pd.read_csv('puntaje.csv')

grupo_a = df[df['embalaje'] == 'A']['puntuacion']
grupo_b = df[df['embalaje'] == 'B']['puntuacion']

test = st.ttest_ind(grupo_a, grupo_b)

print(f"Valor P-Value: {test.pvalue}")