import matplotlib.pyplot as plt

semanas = [1, 2, 3, 4]
kilometros = [2, 5, 4, 8]

plt.plot(semanas, kilometros)

plt.title("Progreso de entrenamiento")
plt.xlabel("Semana")
plt.ylabel("Kilómetros recorridos")

plt.show()