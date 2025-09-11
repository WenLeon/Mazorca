from __future__ import annotations

from pydantic import BaseModel


class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
