from __future__ import annotations

from typing import Any

import httpx


class SupabaseAdapter:
    """Cliente ligero para interactuar con Supabase mediante REST y RPC."""

    def __init__(self, url: str, key: str, *, transport: httpx.AsyncBaseTransport | None = None) -> None:
        self._url = url.rstrip("/")
        self._headers = {
            "apikey": key,
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        }
        self._transport = transport

    async def get_table(self, table: str) -> list[dict[str, Any]]:
        """Obtiene todas las filas de una tabla."""
        async with httpx.AsyncClient(base_url=self._url, headers=self._headers, transport=self._transport) as client:
            response = await client.get(f"/rest/v1/{table}", params={"select": "*"})
            response.raise_for_status()
            return response.json()

    async def call_rpc(self, function: str, params: dict[str, Any] | None = None) -> Any:
        """Ejecuta una función RPC de Supabase."""
        async with httpx.AsyncClient(base_url=self._url, headers=self._headers, transport=self._transport) as client:
            response = await client.post(f"/rest/v1/rpc/{function}", json=params or {})
            response.raise_for_status()
            return response.json()
