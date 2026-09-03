from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Producto(Base):
    __tablename__ = "productos"
    
    id: Mapped[int] =  mapped_column(primary_key=True)
    nombre: Mapped[str]
    descripcion: Mapped[str]
    precio: Mapped[int]
    stock: Mapped[int]
    

DB_URI = "sqlite:///db.sqlite3"
engine = create_engine(DB_URI)
print(engine)

Base.metadata.create_all(engine)