class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

        if cantidad > 0:
            print(f"Se han agregado {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}")
        else:
            print(f"Se han vendido {-cantidad} unidades de {self.nombre}. Stock actual: {self.stock}")

producto = Producto("Laptop", 1500.00, 10)
producto.actualizar_stock(-1)  # Vender una laptop
producto.actualizar_stock(5)   # Agregar 5 laptops al stock
