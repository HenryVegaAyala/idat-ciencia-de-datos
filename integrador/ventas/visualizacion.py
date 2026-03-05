import matplotlib.pyplot as plt

def visualizar_datos(datos_completos):

    print("Generando gráficos...")

    marco = plt.subplots(1,2, figsize=(12,5))

    ax1 = marco[1][0] # Primer grafico (izquierda) - Histograma de edades
    ax2 = marco[1][1] # Segundo grafico (derecha) - Montos Premium vs Normal

    # Grafico 1: Histograma de edades
    ax1.hist(datos_completos["edad"], bins=5, color="skyblue", edgecolor="black")
    ax1.set_title("¿De qué edad son nuestros clientes?")
    ax1.set_xlabel("Edad")
    ax1.set_title("Cantidad de clientes")

    # Grafico 2: Montos Premium vs Normal
    ax2.hist(datos_completos[datos_completos["compro_premium"] == 0]["monto_comprado"], alpha=0.5, label="Normales", color="red")
    ax2.hist(datos_completos[datos_completos["compro_premium"] == 1]["monto_comprado"], alpha=0.5, label="Premium", color="green")
    ax2.set_title("Gastos: Clientes Normales vs Premium")
    ax2.set_xlabel("Monto ($)")
    ax2.set_title("Cantidad de clientes")
    ax2.legend()

    plt.tight_layout() # Se acomoda todo el contenido para que se vea bonito y ordenado.
    plt.show()