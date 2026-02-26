import matplotlib.pyplot as plt

# ventas = [10, 25, 18, 40, 32]
# plt.plot(ventas)
# plt.show()

horas = [1, 2, 3, 4]
cantidad = [10, 20, 25, 30]

plt.plot(horas, cantidad)
plt.title("Cantidad de ventas por hora")
plt.xlabel("Horas")
plt.ylabel("Cantidad de ventas")
plt.show()