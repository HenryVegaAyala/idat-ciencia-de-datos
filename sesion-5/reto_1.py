import matplotlib.pyplot as plt

edades = [20, 22, 21, 25, 30, 35, 18, 19, 40, 45, 22, 23, 21]

# Crear un histograma de las edades
plt.hist(edades, bins=5, color="skyblue", edgecolor="black")
plt.title('Distribución de Edades')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.show()