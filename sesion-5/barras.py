import matplotlib.pyplot as plt

ciudades = ["Lima", "Cuzco", "Arequipa"]
ventas = [500, 300, 450]

plt.bar(ciudades, ventas, color=["orange", "green", "blue"])
plt.title("Ventas por Ciudad")
plt.xlabel("Ciudad")
plt.ylabel("Ventas")
plt.show()