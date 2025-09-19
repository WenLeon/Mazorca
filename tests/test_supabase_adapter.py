import httpx
import pytest

from mazorca.adapters.supabase import SupabaseAdapter


@pytest.mark.asyncio
async def test_get_table() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/rest/v1/productos"
        return httpx.Response(200, json=[{"id": 1, "nombre": "Maíz", "precio": 1000}])

    transport = httpx.MockTransport(handler)
    adapter = SupabaseAdapter("https://example.supabase.co", "clave", transport=transport)
    datos = await adapter.get_table("productos")
    assert datos[0]["nombre"] == "Maíz"
