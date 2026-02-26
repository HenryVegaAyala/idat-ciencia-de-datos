import matplotlib.pyplot as plt

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
temperatura_maxima = [25, 28, 26, 30, 31]
temperatura_minima = [15, 14, 16, 18, 17]

plt.plot(dias, temperatura_minima, color="green", label="Temperatura minima")
plt.plot(dias, temperatura_maxima, color="red", label="Temperatura maxima")

plt.title("Temperatura maxima")
plt.xlabel("Dias")
plt.ylabel("Temperatura")

plt.legend()
plt.show()