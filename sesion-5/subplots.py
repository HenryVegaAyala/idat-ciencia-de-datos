import matplotlib.pyplot as plt

# plt.figure(figsize=(10, 5))
#
# # datos de lineales
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
#
# plt.plot(x, y)
# plt.title("Grafico de linea")
# plt.xlabel("Eje X")
# plt.ylabel("Eje Y")
# # plt.show()
#
# # datos de barras
# categorias = ['A', 'B', 'C', 'D']
# valores = [10, 15, 7, 12]
#
# plt.bar(categorias, valores)
# plt.title("Grafico de categoria")
# plt.xlabel("Categoria")
# plt.ylabel("Valor")
# plt.show()

x = [1, 2, 3, 4, 5]
y_linea = [2, 4, 6, 8, 10]  # para grafico de linea
y_barras = [5, 3, 7, 2, 6]  # para grafico de barras
y_puntos = [4, 5, 2, 7, 9]  # para grafico de puntos

plt.figure(figsize=(20, 10))

plt.bar(x, y_barras, color="lightblue", label="Barras", alpha=0.7)
plt.plot(x, y_linea, color="green", marker="o", label="Linea", alpha=0.7)
plt.scatter(x, y_puntos, color="red", label="Puntos", alpha=0.7)

plt.title("Grafico combinado")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.show()