import matplotlib.pyplot as plt

tienda_A = [10, 15, 20]
tienda_b = [5,25,10]

plt.plot(tienda_A, label='Tienda A')
plt.plot(tienda_b, label='Tienda B')

plt.legend()

plt.show()