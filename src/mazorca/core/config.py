from __future__ import annotations

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Configuración del proyecto cargada desde variables de entorno."""

    supabase_url: str
    supabase_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
