
# API
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from modelos import Producto
from schemas import ProductoCreate, ProductoUpdate

engine = create_engine("postgresql+psycopg:///productos")

app = FastAPI()
Session = sessionmaker(engine)

@app.get("/productos", status_code=200)
def listar_productos():
    with Session() as session:
        productos = session.execute(select(Producto)).scalars().all()
        return productos

@app.post("/productos/", status_code=201)
def insertar_producto(producto: ProductoCreate):
    with Session() as session:

        nuevo_producto = Producto(**producto.model_dump()) #Producto(nombre = producto.nombre, precio = producto.precio)
        session.add(nuevo_producto)
        session.commit()
        session.refresh(nuevo_producto)
        return nuevo_producto
       
@app.get("/productos/{producto_id}", status_code=200)
def obtener_producto(producto_id: int):
    with Session() as session:
        producto = session.get(Producto, producto_id)
        if producto is None:
            raise HTTPException(status_code=404, detail="producto no encontrado")
        return producto

@app.delete("/productos/{id}", status_code=204)
def eliminar_producto(id: int):
    with Session() as session:
        producto = session.get(Producto, id)
        if not producto:
            raise HTTPException(status_code=404, detail = "Producto no encontrado")
        session.delete(producto)
        session.commit()
        return {"mensaje": "Producto eliminado correctamente"}


@app.patch("/productos/{id}", status_code=200)
def actualizar_producto(id: int,data_actualizar: ProductoUpdate):
    with Session() as session:
        producto = session.get(Producto, id)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        
        print(data_actualizar.model_dump(exclude_unset=True))
        dict_act = data_actualizar.model_dump(exclude_unset=True)
        for clave, valor in dict_act.items():
            setattr(producto, clave, valor)
        session.commit()
        session.refresh(producto)
        return producto
        
        
    # get categorias
    # insert categorias
    
    
    
