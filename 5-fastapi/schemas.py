from pydantic import BaseModel

class ProductoCreate(BaseModel):
    nombre: str
    precio: int

class ProductoUpdate(BaseModel):
    nombre: str | None = None
    precio: int | None = None