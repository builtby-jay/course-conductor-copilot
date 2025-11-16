import os
import json
from openai import OpenAI


DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.1-mini")


def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        # This makes it very clear what’s wrong if the var isn’t set
        raise RuntimeError(
            "OPENAI_API_KEY is not set. "
            "Set it in your shell before running uvicorn, e.g.: "
            "$env:OPENAI_API_KEY='sk-...' in PowerShell."
        )
    return OpenAI(api_key=api_key)


def call_llm(prompt: str) -> str:
    """
    Call OpenAI with a simple text prompt and return the output text.
    """
    client = get_client()
    response = client.responses.create(
        model=DEFAULT_MODEL,
        input=prompt,
    )
    return response.output_text


def call_llm_json(prompt: str) -> dict:
    """
    Same as call_llm, but expects JSON and parses it.
    """
    text = call_llm(prompt)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"raw": text}
