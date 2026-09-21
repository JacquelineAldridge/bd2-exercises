from sqlalchemy import ForeignKey, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

class Base(DeclarativeBase):
    pass

class Producto(Base):
    __tablename__ = "productos"
    
    id: Mapped[int] =  mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(30), nullable=False,unique=False)
    descripcion: Mapped[str | None] = mapped_column(String(250), nullable=True)
    precio: Mapped[int] = mapped_column(Integer)
    stock: Mapped[int] = mapped_column(Integer, default= 0 )
    #categoria: Mapped[str] = mapped_column(String)
        
    # Relaciones
    detalle: Mapped["DetalleProducto"] = relationship(back_populates="producto", uselist=False)
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"))
    categoria: Mapped["Categoria"] = relationship(back_populates="productos") 
    
    
    def __str__(self):
        return f"{self.nombre}: {self.precio} ({self.stock} en stock)"
    
class DetalleProducto(Base):
    __tablename__ = "detalles_productos"
    id: Mapped[int] = mapped_column(primary_key=True)
    peso: Mapped[int] = mapped_column(Integer)
    color: Mapped[str] = mapped_column(String(20))
    material: Mapped[str] = mapped_column(String(20))
    lote: Mapped[str] = mapped_column(String(50))
    
    # Relaciones
    producto_id: Mapped[int] = mapped_column(ForeignKey("productos.id"), unique=True)
    producto: Mapped["Producto"] = relationship(back_populates="detalle")
    
    def __str__(self):
        return f"[{self.producto.nombre}] {self.peso}gr , {self.color} - (lote: {self.lote})"

class Categoria(Base):
    __tablename__ = "categorias"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(30))
    
    # Relaciones
    productos: Mapped[list["Producto"]] = relationship(back_populates="categoria")
    
    
DB_URI = "sqlite:///productos_relaciones.sqlite3"
engine = create_engine(DB_URI)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(engine)

categorias = [
    Categoria(nombre="Periféricos"),
    Categoria(nombre="Monitores"),
    Categoria(nombre="Componentes"),
    Categoria(nombre="Almacenamiento"),
    Categoria(nombre="Audio"),
    Categoria(nombre="Impresoras"),
    Categoria(nombre="Computación"),
]
c1,c2,c3,c4,c5,c6,c7 = categorias

p1 = Producto(nombre = "Notebook", precio = 899990, stock= 15, categoria=c7)
#d1 = DetalleProducto(peso= 1500, color="gris", material="Aluminio", lote="TEC001", producto_id = 1)
d1 = DetalleProducto(peso= 1500, color="gris", material="Aluminio", lote="TEC001", producto = p1)

productos = [
    Producto(nombre="Mouse inalámbrico", precio=19990, stock=40, categoria=c1),
    Producto(nombre="Teclado mecánico", precio=59990, stock=25, categoria=c1),
    Producto(nombre="Monitor 27 pulgadas", precio=249990, stock=10, categoria=c2),
    Producto(nombre="Memoria RAM 16GB", precio=45990, stock=30, categoria=c3),
    Producto(nombre="Tarjeta de video", precio=499990, stock=8, categoria=c3),
    Producto(nombre="Disco duro externo", precio=69990, stock=20, categoria=c4),
    Producto(nombre="Audífonos inalámbricos", precio=79990, stock=18, categoria=c5),
    Producto(nombre="Webcam HD", precio=39990, stock=22, categoria=c1),
    Producto(nombre="Impresora multifuncional", precio=189990, stock=7, categoria=c6),
]

p2,p3,p4,p5,p6,p7,p8,p9,p10 = productos
detalles = [
    DetalleProducto(peso=120, color="Negro", material="Plástico", lote="TEC002", producto=p2),
    DetalleProducto(peso=800, color="Negro", material="Plástico", lote="TEC003", producto=p3),
    DetalleProducto(peso=3000, color="Negro", material="Plástico", lote="TEC004", producto=p4),
    DetalleProducto(peso=50, color="Negro", material="Metal", lote="TEC005", producto=p5),
    DetalleProducto(peso=30, color="Negro", material="Circuito", lote="TEC006", producto=p6),
    DetalleProducto(peso=900, color="Negro", material="Metal", lote="TEC007", producto=p7),
    DetalleProducto(peso=350, color="Negro", material="Plástico", lote="TEC008", producto=p8),
    DetalleProducto(peso=150, color="Negro", material="Plástico", lote="TEC009", producto=p9),
    DetalleProducto(peso=5000, color="Blanco", material="Metal", lote="TEC010", producto=p10),
]


with Session() as session:
    session.add(p1)
    session.add(d1)
    session.add_all(productos)
    session.add_all(detalles)
    session.add_all(categorias)
    session.commit()
    
    detalle_1 = session.get(DetalleProducto, 1)
    print(detalle_1)
    
    print(f"{'-'*25} Todos los productos con sus categorias {'-'*25}")
    productos = session.execute(select(Producto)).scalars().all()
    for producto in productos:
        print(f"{producto.nombre} --> {producto.categoria.nombre} (lote: {producto.detalle.lote})")

