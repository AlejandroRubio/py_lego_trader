from pydantic import BaseModel
import pandas as pd

class lego_model(BaseModel):
    ID: int
    Nombre: str
    Link: str	
    Unidades: int
    PrecioCompra: float
    PrecioActual: float
    Beneficio: float
    Rentabilidad: float