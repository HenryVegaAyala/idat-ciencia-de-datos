class Cliente:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def comprar(self, producto, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            # self.saldo = self.saldo - monto
            print(f"{self.nombre} ha comprado por ${monto} el producto {producto} queda un saldo pendiente de ${self.saldo}.")
        else:
            print(f"{self.nombre} no tiene suficiente saldo para comprar por ${monto} el producto {producto}, solo tiene ${self.saldo}.")

# Ejemplo de uso
cliente1 = Cliente("Veronica", 100)
cliente1.comprar("Mac ", 90)
cliente1.comprar("Iphone",100)

print("")

cliente2 = Cliente("Bruno", 600)
cliente2.comprar("Motocar", 200)
cliente2.comprar("Xiomi", 100)
cliente2.comprar("Play Station", 200)