# Ejecutor del programa

from ventas.datos import cargar_datos, cruzar_datos
from ventas.estadistica import analisis_estadistico
from ventas.visualizacion import visualizar_datos
from ventas.modelos import modelos_predictivos

def main():
    clientes, compras = cargar_datos()
    df = cruzar_datos(clientes, compras)
    analisis_estadistico(df)
    visualizar_datos(df)
    modelos_predictivos(df)

if __name__ == '__main__':
    main()
