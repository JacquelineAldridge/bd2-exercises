from sqlalchemy import Integer, String, create_engine, select, update
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

class Base(DeclarativeBase):
    pass

class Producto(Base):
    __tablename__ = "productos"
    
    id: Mapped[int] =  mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(30), nullable=False,unique=False)
    descripcion: Mapped[str | None] = mapped_column(String(250), nullable=True)
    precio: Mapped[int] = mapped_column(Integer)
    stock: Mapped[int] = mapped_column(Integer, default= 0 )
    categoria: Mapped[str] = mapped_column(String)
    
    def __str__(self):
        return f"{self.nombre}: {self.precio} ({self.stock} en stock)"
    

DB_URI = "sqlite:///db.sqlite3"
engine = create_engine(DB_URI)
print(engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

producto_1 = Producto(nombre = "Mouse", descripcion = "MX anywhere 3", precio=50000, stock=30, 
                      categoria="Computación")
print(producto_1)

producto_2 = Producto(nombre = "Teclado", descripcion="Mecánico", precio=30000, stock=10, categoria="Computación")
Session = sessionmaker(engine)

productos = [
Producto(nombre="Laptop", descripcion="Laptop para uso diario", precio=599990, stock=10, categoria="Tecnología"),
Producto(nombre="Mouse 2", descripcion="Mouse inalámbrico", precio=19990, stock=25, categoria="Tecnología"),
Producto(nombre="Teclado", descripcion="Teclado mecánico RGB", precio=45990, stock=15, categoria="Tecnología"),
Producto(nombre="Audífonos", descripcion="Audífonos Bluetooth", precio=29990, stock=20, categoria="Audio"),
Producto(nombre="Monitor", descripcion="Monitor Full HD 24 pulgadas", precio=129990, stock=8, categoria="Tecnología"),
Producto(nombre="Mochila", descripcion="Mochila para notebook", precio=34990, stock=12, categoria="Accesorios"),
Producto(nombre="Cuaderno", descripcion="Cuaderno universitario", precio=4990, stock=50, categoria="Librería"),
Producto(nombre="Lápiz", descripcion="Lápiz pasta azul", precio=990, stock=100, categoria="Librería"),
Producto(nombre="Botella", descripcion="Botella reutilizable", precio=8990, stock=30, categoria="Hogar"),
Producto(nombre="Polera", descripcion="Polera de algodón", precio=14990, stock=18, categoria="Ropa")]

with Session() as session:
    # insertar registros
    
    # session.add(producto_1) # Añadir un registro
    session.add_all([producto_1, producto_2])
    # session.add_all([
    #     Producto(nombre = "Teclado", descripcion="Mecánico", precio=30000, stock=10, categoria="Computación"),
    #     Producto(nombre = "Mouse", descripcion = "MX anywhere 3", precio=50000, stock=30, 
    #                   categoria="Computación")
    # ])
    
    print(f"{'-'*25} Consultas {'-'*25}")
    print(f"{'-'*25} Obtener todos los registro {'-'*25}")

    query = select(Producto)
    results = session.execute(query).scalars().all()
    for result in results:
        print(result)
        print(result.nombre)
        
    print(f"{'-'*25} Obtener el primer registro {'-'*25}")
    query = select(Producto)
    result_first = session.execute(query).scalars().first()
    print(result_first)
    
    print(f"{'-'*25} Obtener el primer registro y dar un error si es que hay más de uno {'-'*25}")
    # query = select(Producto)
    # result_one = session.execute(query).scalars().one() # Esto da error porque hay más de un registro
    # print(result_one)
    
    session.add_all(productos)
    session.commit()
    
    print(f"{'-'*25} Obtener los registros con un precio mayor a 15000 {'-'*25}")
    query = select(Producto).where(Producto.precio > 15000)
    results = session.execute(query).scalars().all()
    for producto in results:
        print(producto)
        
    print(f"{'-'*25} Obtener los registros con un precio mayor a 15000 (ordenado) {'-'*25}")
    query = (select(Producto)
             .where(Producto.precio > 15000)
             #.order_by(Producto.precio) # de menor a mayor
             .order_by(Producto.precio.desc()) # de mayor a menor
             )
    
    results = session.execute(query).scalars().all()
    for producto in results:
        print(producto)

    print(f"{'-'*25} Obtener todos los registros que empiecen con M {'-'*25}")
    query = select(Producto).where(Producto.nombre.like("M%"))
    results = session.execute(query).scalars().all()
    for producto in results:
        print(producto)
        
    print(f"{'-'*25} Obtener todos los registros que no contengan la z {'-'*25}")
    query = select(Producto).where(~Producto.nombre.like("%z%"))
    results = session.execute(query).scalars().all()
    for producto in results:
        print(producto)
      
    print(f"{'-'*25} Recuperar el registro con ID 2 {'-'*25}")  
    query = session.get(Producto, 2) # recuperar por clave primaria
    print(query)
    
    print(f"{'-'*25} Actualizar registros {'-'*25}")
    polera = session.get(Producto, 12)
    print(polera)
    polera.precio = polera.precio * 1.2 
    session.add(polera)
    session.commit()
    polera_actulizada = session.get(Producto, 12)
    print(polera_actulizada)
    
    query  = (
        update(Producto)
        .where(Producto.nombre == "Botella")
        .values(precio = 12345)
    )
    print(query)
    session.execute(query)
    session.commit()
    
    query = (
        update(Producto)
        .values(precio = Producto.precio * 5)
    )
    session.execute(query)
    session.commit()
    
    print(f"{'-'*25} Eliminar registros {'-'*25}")
    
    lapiz = session.get(Producto, 10)
    session.delete(lapiz)
    session.commit()  
    
    
    
    