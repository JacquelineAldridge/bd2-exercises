print(f"{'-'*25} Ejercicios {'-'*25}")

class Producto:
    def __init__(self, nombre, precio, STOCK):
        self.nombre = nombre
        self.precio = precio
        self.__stock = STOCK # atributo privado
        
    def mostrar_info(self):
        return f"Nombre del producto {self.nombre} --> ${self.precio} ({self.__stock} en stock)"
    
    def aplicar_descuento(self, porcentaje):
        desc = self.precio * porcentaje / 100
        self.precio = self.precio - desc
    
    def consultar_stock(self):
        return self.__stock
    
    def aumentar_stock(self,cantidad):
        if cantidad > 0:
            self.__stock = self.__stock + cantidad
        else:
            print("Error: la cantidad debe ser positiva")
    
    def vender(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock = self.__stock - cantidad
            print(f"{cantidad} productos vendidos")
        else:
            print("Error: no hay suficiente stock")
    
    def __str__(self):
        return f"{self.nombre} ${self.precio} {self.__stock}"

class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, stock, garantia):
        super().__init__(nombre, precio,stock)
        self.garantia = garantia

    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: {self.precio} (hay {self.consultar_stock()} - {self.garantia} meses de garantia)"

class ProductoAlimenticio(Producto):
    def __init__(self, nombre, precio, stock,fecha_vencimiento):
        super().__init__(nombre,precio,stock)
        self.fecha_vencimiento = fecha_vencimiento
        
    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: {self.precio} (hay {self.consultar_stock()} - fecha de vencimiento: {self.fecha_vencimiento} )"

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        
    def agregar_productos(self, producto):
        if isinstance(producto, Producto):
            self.productos.append(producto)
            print(f"Producto '{producto.nombre}' agregado. ")
        else:
            print(f"Error solo se pueden añadir productos (se esta intentando añadir un: {type(producto)})")
        
    def mostrar_catalogo(self):
        print(f" --- Catálogo de {self.nombre} --- ")
        for producto in self.productos:
            print(producto.mostrar_info())
    
    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                print(f"Producto encontrado: {producto.nombre}")
                return producto
        print("Producto no encontrado")

if __name__ == "__main__":
    print("Archivo de clases")