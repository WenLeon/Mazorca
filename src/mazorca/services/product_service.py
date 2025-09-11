from __future__ import annotations

from typing import Sequence

from ..adapters.supabase import SupabaseAdapter
from ..models.producto import Producto


class ProductService:
    """Casos de uso relacionados con productos."""

    def __init__(self, adapter: SupabaseAdapter) -> None:
        self._adapter = adapter

    async def listar(self) -> Sequence[Producto]:
        datos = await self._adapter.get_table("productos")
        return [Producto(**item) for item in datos]
