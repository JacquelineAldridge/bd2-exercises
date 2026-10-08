
# API
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, select
from sqlalchemy.orm import selectinload, sessionmaker

from modelos import Categoria, Producto, Proveedor
from schemas import ProductoCreate, ProductoUpdate, CategoriaCreate, ProveedorCreate

engine = create_engine("postgresql+psycopg:///productos")

app = FastAPI()
Session = sessionmaker(engine)

@app.get("/productos", status_code=200, tags=["Productos"])
def listar_productos():
    with Session() as session:
        productos = session.execute(select(Producto)
                                    .options(selectinload(Producto.proveedores))
                                    ).scalars().all()
        return productos

@app.post("/productos/", status_code=201, tags=["Productos"])
def insertar_producto(producto: ProductoCreate):
    with Session() as session:

        nuevo_producto = Producto(**producto.model_dump(exclude={"proveedor_ids"})) #Producto(nombre = producto.nombre, precio = producto.precio)
        if producto.proveedor_ids:
            nuevos_proveedores = session.execute(select(Proveedor)
                                        .where(Proveedor.id.in_(producto.proveedor_ids))
                                        ).scalars().all()
            nuevo_producto.proveedores = nuevos_proveedores
        session.add(nuevo_producto)
        session.commit()
        session.refresh(nuevo_producto)
        return nuevo_producto
       
@app.get("/productos/{producto_id}", status_code=200, tags=["Productos"])
def obtener_producto(producto_id: int):
    with Session() as session:
        producto = session.get(Producto, producto_id)
        if producto is None:
            raise HTTPException(status_code=404, detail="producto no encontrado")
        return producto

@app.delete("/productos/{id}", status_code=204, tags=["Productos"])
def eliminar_producto(id: int):
    with Session() as session:
        producto = session.get(Producto, id)
        if not producto:
            raise HTTPException(status_code=404, detail = "Producto no encontrado")
        session.delete(producto)
        session.commit()
        return {"mensaje": "Producto eliminado correctamente"}


@app.patch("/productos/{id}", status_code=200, tags=["Productos"])
def actualizar_producto(id: int,data_actualizar: ProductoUpdate):
    with Session() as session:
        producto = session.get(Producto, id)
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        
        print(data_actualizar.model_dump(exclude_unset=True))
        dict_act = data_actualizar.model_dump(exclude_unset=True, exclude = {"proveedor_ids"})
        for clave, valor in dict_act.items():
            setattr(producto, clave, valor)
            
        if data_actualizar.proveedor_ids is not None:
            nuevos_proveedores = session.execute(select(Proveedor)
                                        .where(Proveedor.id.in_(data_actualizar.proveedor_ids))
                                        ).scalars().all()
        
            producto.proveedores = nuevos_proveedores
        session.commit()
        session.refresh(producto)
        return producto

# Categorias
@app.get("/categorias", status_code= 200, tags=["Categorias"])
def listar_categorias():
    with Session() as session:
        categorias = session.execute(select(Categoria)).scalars().all()
        return categorias
    
@app.post("/categorias/",status_code=201, tags=["Categorias"])
def insertar_categoria(categoria: CategoriaCreate):
    with Session() as session:
        nueva_categoria = Categoria(**categoria.model_dump())
        session.add(nueva_categoria)
        session.commit()
        session.refresh(nueva_categoria)
        return nueva_categoria

# Proveedores
@app.post("/proveedores", tags=["Proveedores"])
def insertar_proveedor(proveedor: ProveedorCreate):
    with Session() as session:
        nuevo_proveedor = Proveedor(**proveedor.model_dump())
        session.add(nuevo_proveedor)
        session.commit()
        session.refresh(nuevo_proveedor)
        return nuevo_proveedor
    
@app.get("/proveedores", status_code= 200, tags=["Proveedores"])
def listar_proveedores():
    with Session() as session:
        categorias = session.execute(select(Proveedor)).scalars().all()
        return categorias

    
    
