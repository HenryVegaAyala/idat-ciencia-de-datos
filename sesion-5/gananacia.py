import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('salarios.csv')

plt.bar(df["nombre"], df["sueldo"], color="blue")
plt.title("Ganancia")
plt.xlabel("nombre")
plt.ylabel("sueldo")
plt.grid(True)
# plt.show()
plt.savefig("ganancia.png")