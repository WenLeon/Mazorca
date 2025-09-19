from __future__ import annotations

from typing import Any

from ..adapters.supabase import SupabaseAdapter


class VentaService:
    """Casos de uso para ventas."""

    def __init__(self, adapter: SupabaseAdapter) -> None:
        self._adapter = adapter

    async def confirmar(self, venta_id: int) -> Any:
        return await self._adapter.call_rpc("confirmar_venta", {"p_venta_id": venta_id})

    async def recomputar_totales(self, venta_id: int) -> Any:
        return await self._adapter.call_rpc("recompute_sale_totals", {"p_venta_id": venta_id})
