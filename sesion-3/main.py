import numpy as np

# Lectura de una lista
lista = [1, 2, 3, 4, 5]
array = np.array(lista)

# print(array)
# print(np.zeros(5))
# print(np.ones(6))
# print(np.arange(0,10,4))

data = np.array([10, 20, 30, 40, 50])

subnet = data[1:4]
# print(subnet)

data[0:2] = 0
# print(data)

edades = np.array([15, 20, 18, 12, 30, 25])

es_mayor = edades >= 18
# print(edades)
# print(es_mayor)
# print(edades[es_mayor])

temps = np.array([22, 21, 23, 90, 22, 20, 105, 21])

# Temperaturas mayor a 50
errores = temps < 50
resultado = temps[errores]

print(resultado)
print(resultado.size)
