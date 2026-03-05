import pathlib
import pandas as pd

__DATA_DIR = pathlib.Path(__file__).resolve().parents[1] / "data"

def cargar_datos():
    print("Cargando datos...")
    clientes = pd.read_csv(__DATA_DIR / "clientes.csv")
    compras = pd.read_csv(__DATA_DIR / "compras.csv")

    print("Datos cargados exitosamente.")
    return clientes, compras

def cruzar_datos(clientes, compras):
    print("Cruzando datos...")
    resultado = pd.merge(clientes, compras, on="id_cliente", how="inner")
    print("Datos cruzados exitosamente.")
    return resultado