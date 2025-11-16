from __future__ import annotations

from typing import List

# Simple CORS origin list – no Pydantic, no BaseSettings needed.
CORS_ORIGINS: List[str] = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
