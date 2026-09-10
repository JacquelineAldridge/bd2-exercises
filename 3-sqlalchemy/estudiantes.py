from datetime import datetime

from sqlalchemy import Boolean, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
engine = create_engine("sqlite:///estudiantes.sqlite3")

class Base(DeclarativeBase):
    pass

class Estudiante(Base):
    __tablename__ = "estudiantes"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    rut: Mapped[str] = mapped_column(String(12))
    nombre: Mapped[str] = mapped_column(String(50))
    apellido: Mapped[str] = mapped_column(String(50))
    carrera: Mapped[str] = mapped_column(String(100))
    año_ingreso: Mapped[int] = mapped_column(Integer)
    activo: Mapped[bool] = mapped_column(Boolean,default=True )
    fecha_registro: Mapped[datetime] = mapped_column(default=datetime.now)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.carrera}"
    
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(engine)

estudiantes = [
        Estudiante(rut="12345678-9", nombre="Juan", apellido="Pérez", carrera="Ingeniería Civil", año_ingreso=2024),
        Estudiante(rut="98765432-1", nombre="María", apellido="González", carrera="Medicina", año_ingreso=2024),
        Estudiante(rut="11223344-5", nombre="Carlos", apellido="Rojas", carrera="Psicología", año_ingreso=2023),
        Estudiante(rut="55667788-9", nombre="Ana", apellido="Silva", carrera="Derecho", año_ingreso=2024),
        Estudiante(rut="99887766-3", nombre="Luis", apellido="Torres", carrera="Arquitectura", año_ingreso=2023),
        Estudiante(rut="44556677-8", nombre="Carmen", apellido="López", carrera="Ingeniería Civil", año_ingreso=2022),
        Estudiante(rut="33445566-7", nombre="Pedro", apellido="Martín", carrera="Medicina", año_ingreso=2023),
        Estudiante(rut="77889900-1", nombre="Laura", apellido="Díaz", carrera="Psicología", año_ingreso=2024),
    ]
with Session() as session:
    session.add_all(estudiantes)
    session.commit()