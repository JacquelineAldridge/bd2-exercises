from pydantic import BaseModel

class ProductoCreate(BaseModel):
    nombre: str
    precio: int
    categoria_id: int | None = None
    proveedor_ids: list[int] | None = None
    
class ProductoUpdate(BaseModel):
    nombre: str | None = None
    precio: int | None = None
    categoria_id: int | None = None
    proveedor_ids: list[int] | None = None
class CategoriaCreate(BaseModel):
    nombre: str
    
class ProveedorCreate(BaseModel):
    nombre: str
    direccion: str
    email: str
    