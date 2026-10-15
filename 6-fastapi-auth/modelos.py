from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Producto(Base):
    __tablename__= "productos"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    precio: Mapped[int] = mapped_column(Integer) 
    
    # Relaciones
    categoria_id: Mapped[int | None] = mapped_column(ForeignKey("categorias.id"), default=None)
    categoria: Mapped["Categoria"] = relationship(back_populates="productos")
    proveedores: Mapped[list["Proveedor"]] = relationship(back_populates="productos", secondary = "productos_proveedores")

class Categoria(Base):
    __tablename__ = "categorias"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(30))
    
    # Relaciones
    productos: Mapped[list["Producto"]] = relationship(back_populates="categoria")
    
class ProductoProveedores(Base):
    __tablename__ = "productos_proveedores"
    producto_id: Mapped[int] = mapped_column(ForeignKey("productos.id"), primary_key=True)
    proveedor_id: Mapped[int] = mapped_column(ForeignKey("proveedores.id"), primary_key=True)
        
class Proveedor(Base):
    __tablename__ = "proveedores"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    direccion:  Mapped[str] = mapped_column(String(150))
    email: Mapped[str] = mapped_column(String(100), unique= True)
    
    # Relaciones
    productos: Mapped[list["Producto"]] = relationship(back_populates="proveedores", secondary = "productos_proveedores")
    