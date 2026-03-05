import pandas as pd
import scipy.stats as st
import numpy as np

df = pd.read_csv('tiempos.csv')

tradicional = df[df['vehiculo'] == 'Tradicional']['minutos']
electrico = df[df['vehiculo'] == 'Electrica']['minutos']

# 1. Intervalo para vehiculos electricos

ic = st.t.interval(0.95, len(electrico)-1, np.mean(electrico), st.sem(electrico))
print(f"Intervalo de confianza para vehículos eléctricos: {ic[0]} y {ic[1]} minutos")

ic = st.t.interval(0.95, len(tradicional)-1, np.mean(tradicional), st.sem(tradicional))
print(f"Intervalo de confianza para vehículos tradicionales: {ic[0]} y {ic[1]} minutos")

test = st.ttest_ind(tradicional, electrico)
print(f"Valor p: {test.pvalue}")