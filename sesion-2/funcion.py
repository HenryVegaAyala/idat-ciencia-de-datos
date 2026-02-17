def calcular_precio_final(precio_base):
    igv = 0.18
    impuesto = precio_base * igv
    precio_final = precio_base + impuesto
    return precio_final

producto = calcular_precio_final(100)
print(f"El precio final del producto es: S/ {producto}")

def convertir_soles(monto_dolares):
    tipo_de_cambio = 3.80
    monto_soles = monto_dolares * tipo_de_cambio
    return monto_soles

monto_en_soles = convertir_soles(50)
print(f"La conversión a soles es: S/ {monto_en_soles}")

