import numpy as np
import matplotlib.pyplot as plt

# datos = np.random.normal(50, 10, 1000)
# print(datos)
#
# plt.hist(datos, bins=30, density=True, alpha=0.5)
#
# # curva de densidad
# plt.axvline(np.mean(datos), color="red", label="Media")
#
# plt.legend()
# plt.title("Histograma con curva de densidad")
# plt.show()

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]

# Datos de gastos (cada lista representa un tipo de gasto)
gastos_alquiler = [500, 520, 510, 530, 540]
gastos_comida = [1500, 320, 310, 300, 330]
gastos_transporte = [100, 110, 105, 115, 120]

# Ingresos mensuales
ingresos = [1200, 1300, 1250, 1400, 1500]

# Crear el gráfico de barras para los gastos
plt.plot(meses, gastos_alquiler, label="Alquiler")
plt.plot(meses, gastos_comida, label="Comida")
plt.plot(meses, gastos_transporte, label="Transporte")

# Crear el gráfico de barras para los ingresos
plt.plot(meses, ingresos, label="Ingresos")

plt.title("Gastos e Ingresos Mensuales")
plt.xlabel("Meses")
plt.ylabel("Cantidad (S/.)")
plt.legend()
plt.grid()
plt.show()