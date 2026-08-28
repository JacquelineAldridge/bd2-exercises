print(f"{'-'*25} Ejercicios {'-'*25}")

class Producto:
    def __init__(self, nombre, precio, STOCK):
        self.nombre = nombre
        self.precio = precio
        self.stock = STOCK
        
    def mostrar_info(self):
        return f"Nombre del producto {self.nombre} --> ${self.precio} ({self.stock} en stock)"
    
    def aplicar_descuento(self, porcentaje):
        desc = self.precio * porcentaje / 100
        self.precio = self.precio - desc
    
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock = self.stock - cantidad
            print(f"{cantidad} productos vendidos")
        else:
            print("Error: no hay suficiente stock")
    
    def __str__(self):
        return f"{self.nombre} ${self.precio} {self.stock}"

class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, stock, garantia):
        super().__init__(nombre, precio,stock)
        self.garantia = garantia

    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: {self.precio} (hay {self.stock} - {self.garantia} meses de garantia)"

class ProductoAlimenticio(Producto):
    def __init__(self, nombre, precio, stock,fecha_vencimiento):
        super().__init__(nombre,precio,stock)
        self.fecha_vencimiento = fecha_vencimiento
        
    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: {self.precio} (hay {self.stock} - fecha de vencimiento: {self.fecha_vencimiento} )"

producto = Producto("Laptop",700000, 8)
producto_2 = Producto(nombre = "Teclado", STOCK=10, precio= 20000)
print(producto)
print(producto.mostrar_info())
producto.aplicar_descuento(20)
print(producto.mostrar_info())
producto.vender(3)
print(producto.mostrar_info())

producto_el_1 = ProductoElectronico("Reloj inteligente", 200000, 10, 6)
print(producto_el_1.mostrar_info())
producto_al_1= ProductoAlimenticio("Pan",1000, 20, "28/08/2026")
print(producto_al_1.mostrar_info())