from __future__ import annotations

from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import CORS_ORIGINS
from .models import (
    CoursePage,
    IngestPagesRequest,
    GenerateUpdatesRequest,
    GenerateUpdatesResponse,
    QARequest,
    QAResponse,
)
from .llm_client import call_llm
from .course_loader import load_course_pages


app = FastAPI(title="Course Conductor – AI Ops Copilot")

# Pre-loaded course pages from backend/data/course_pages.json
COURSE_PAGES: List[CoursePage] = [
    CoursePage(**p) for p in load_course_pages()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health():
    return {"status": "ok", "pages_loaded": len(COURSE_PAGES)}


@app.post("/api/ingest-pages")
def ingest_pages(payload: IngestPagesRequest):
    """
    Optional: override course pages from frontend.
    You can ignore this for the demo, since we preload from JSON.
    """
    global COURSE_PAGES
    COURSE_PAGES = payload.pages
    return {"status": "ok", "pages_loaded": len(COURSE_PAGES)}


def build_course_context(max_chars: int = 8000) -> str:
    """
    Flatten the course pages into a single context string for Gemini.
    """
    chunks = []
    for page in COURSE_PAGES:
        chunks.append(f"# {page.title}\n{page.content}\n")
    full = "\n\n".join(chunks)
    if len(full) > max_chars:
        return full[:max_chars] + "\n\n[... truncated ...]"
    return full


@app.post("/api/generate-updates", response_model=GenerateUpdatesResponse)
def generate_updates(payload: GenerateUpdatesRequest):
    """
    Ask Gemini to draft an announcement, email, and/or policy update
    based on a change description, grounded in the course context.
    """
    course_context = build_course_context()

    prompt = f"""
You are an AI teaching operations assistant helping an instructor manage a university course.

Course context:
{course_context}

Audience: {payload.audience}
Requested change:
{payload.change_description}

Write clear, concise drafts for each selected channel. Use the course's tone: professional but approachable.

Return your answer in this JSON structure, with plain text (no markdown) in each field:

{{
  "announcement": "announcement text here or empty string if not requested",
  "email": "email text here or empty string if not requested",
  "policy": "updated policy or Canvas page text here or empty string if not requested"
}}"""

    raw = call_llm(prompt)

    import json

    try:
        data = json.loads(raw)
        return GenerateUpdatesResponse(
            announcement=data.get("announcement") or None,
            email=data.get("email") or None,
            policy=data.get("policy") or None,
        )
    except Exception:
        return GenerateUpdatesResponse(
            announcement=raw.strip() or None,
            email=None,
            policy=None,
        )


@app.post("/api/qa", response_model=QAResponse)
def qa(payload: QARequest):
    """
    Answer student questions about the course, grounded in COURSE_PAGES.
    """
    course_context = build_course_context()

    prompt = f"""
You are an AI assistant for a university course focused on phishing risk and organizational resilience.

Course information:
{course_context}

Student question:
{payload.question}

Answer based ONLY on the course information above. If the question cannot be answered from that info, say so and suggest that the student contact the instructor or check the syllabus. Be concise and student-friendly.
"""

    answer = call_llm(prompt)
    return QAResponse(answer=answer.strip())
