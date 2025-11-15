import os
from pydantic import BaseModel

class Settings(BaseModel):
    llm_api_key: str | None = os.getenv("LLM_API_KEY")
    llm_model: str = os.getenv("LLM_MODEL", "gpt-4.1-mini")  # or Claude model name
    app_name: str = "Course Conductor"

settings = Settings()
