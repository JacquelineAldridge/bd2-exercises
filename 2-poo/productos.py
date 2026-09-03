from clases import Producto, ProductoAlimenticio, ProductoElectronico, Tienda
print(f"{'-'*25} Ejercicios {'-'*25}")     
        
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

print(f"{'-'*25} 1.3 {'-'*25}")
producto_al_1.aumentar_stock(6)
print(producto_al_1.mostrar_info())
producto_al_1.vender(8)
print(producto_al_1.mostrar_info())
print(f"Stock disponible: {producto_al_1.consultar_stock()}")

print(f"{'-'*25} 1.4 {'-'*25}")
productos = [producto_al_1, producto_el_1, producto, producto_2]
print(productos)
for producto_ in productos:
    print(producto_.mostrar_info())
    
productos = [ProductoElectronico("Reloj Inteligente", 2000000, 10, 3),
             ProductoAlimenticio("Pan", 1000, 10,"28/09/2026")
             ]
for producto_ in productos:
    print(producto_.mostrar_info())
    
print("Tienda de productos")
tienda = Tienda("Supermarket express")
tienda.mostrar_catalogo()

producto1= Producto("Cuaderno", 2500, 50)
producto2 = ProductoElectronico("Laptop", 700000, 5, 12)
producto3 = ProductoAlimenticio("Leche", 1200, 20, "10/09/2026")
tienda.mostrar_catalogo()
tienda.agregar_productos(producto1)
tienda.agregar_productos(producto2)
tienda.agregar_productos(producto3)
tienda.mostrar_catalogo()

#tienda.agregar_productos("producto 1")
# Funciones para verificar los tipos de datos
# print(isinstance("producto 1", str))
# print(isinstance("producto 1", int))
# print(isinstance(producto1, Producto))
tienda.agregar_productos("adsd")
tienda.buscar_producto("Leche")
tienda.buscar_producto("Leche Entera")