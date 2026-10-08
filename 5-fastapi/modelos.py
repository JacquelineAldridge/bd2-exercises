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

class Categoria(Base):
    __tablename__ = "categorias"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(30))
    
    # Relaciones
    productos: Mapped[list["Producto"]] = relationship(back_populates="categoria")
    