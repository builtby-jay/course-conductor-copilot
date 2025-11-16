from __future__ import annotations

import os
from typing import Optional

from google import genai  # pip install google-genai


def _get_api_key() -> str:
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY / GOOGLE_API_KEY not set. "
            "Set it before running the server."
        )
    return api_key


GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

_client: Optional[genai.Client] = None


def get_client() -> genai.Client:
    global _client
    if _client is None:
        api_key = _get_api_key()
        _client = genai.Client(api_key=api_key)
    return _client


def call_llm(prompt: str) -> str:
    """
    Simple wrapper around Gemini text generation.

    Takes a single prompt string and returns the model's text response.
    """
    client = get_client()

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )

    if hasattr(response, "text") and response.text:
        return response.text.strip()

    try:
        candidate = response.candidates[0] # type: ignore
        parts = getattr(candidate, "content", candidate).parts # type: ignore
        pieces = []
        for part in parts:
            text = getattr(part, "text", None) or part.get("text", "")
            pieces.append(text)
        return "\n".join(pieces).strip()
    except Exception:
        return str(response)
