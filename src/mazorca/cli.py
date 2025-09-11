from __future__ import annotations

import asyncio
from typing import Sequence

import typer

from .core.config import settings
from .adapters.supabase import SupabaseAdapter
from .services.product_service import ProductService
from .services.venta_service import VentaService
from .models.producto import Producto

app = typer.Typer(help="CLI para gestionar Mazorca")


def _build_adapter() -> SupabaseAdapter:
    return SupabaseAdapter(settings.supabase_url, settings.supabase_key)


@app.command()
def listar_productos() -> None:
    """Muestra todos los productos disponibles."""

    async def _run() -> Sequence[Producto]:
        servicio = ProductService(_build_adapter())
        return await servicio.listar()

    productos = asyncio.run(_run())
    for prod in productos:
        typer.echo(f"{prod.id}: {prod.nombre} - {prod.precio}")


@app.command()
def confirmar_venta(venta_id: int) -> None:
    """Confirma una venta existente."""

    async def _run() -> None:
        servicio = VentaService(_build_adapter())
        resultado = await servicio.confirmar(venta_id)
        typer.echo(resultado)

    asyncio.run(_run())


if __name__ == "__main__":  # pragma: no cover
    app()
