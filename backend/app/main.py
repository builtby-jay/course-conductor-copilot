from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import (
    IngestRequest, ChangeRequest, UpdateResponse,
    QARequest, QAResponse
)
from .storage import replace_pages, build_course_context
from .llm_client import call_llm

app = FastAPI(title="Course Conductor – AI Ops Copilot")

# Allow frontend on localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.post("/api/ingest-pages")
def ingest_pages(req: IngestRequest):
    pages = [p.model_dump() for p in req.pages]
    replace_pages(pages)
    return {"status": "ok", "num_pages": len(pages)}

@app.post("/api/generate-updates", response_model=UpdateResponse)
def generate_updates(req: ChangeRequest):
    context = build_course_context()

    prompt = f"""
You are an AI assistant helping UVA instructors and operations staff keep course
communications in sync.

Course content:
\"\"\"{context}\"\"\"

Requested change:
\"\"\"{req.change_description}\"\"\"

Audience: {req.audience}

Write concise, professional text suitable for higher-education courses.

1) Draft a Canvas-style announcement (with a short title and 1–3 short paragraphs).
2) Draft an email body with the same information (no need to repeat the subject).
3) Draft a policy/syllabus snippet that could replace the relevant section.

Return your answer in this JSON format:
{{
  "announcement": "announcement text here...",
  "email": "email text here...",
  "policy_snippet": "policy text here..."
}}
"""

    raw = call_llm(prompt)

    # For demo, just wrap the output. In a real version you'd parse JSON.
    text = f"LLM OUTPUT JSON:\n{raw}"

    return UpdateResponse(
        announcement=text if "announcement" in req.channels else None,
        email=text if "email" in req.channels else None,
        policy_snippet=text if "policy" in req.channels else None,
    )

@app.post("/api/qa", response_model=QAResponse)
def qa(req: QARequest):
    context = build_course_context()

    prompt = f"""
You are an AI assistant helping answer logistics and policy questions about a course.
Use ONLY the course content to answer.

Course content:
\"\"\"{context}\"\"\"

Question:
\"\"\"{req.question}\"\"\"

Return your answer in JSON:
{{
  "answer": "2–4 sentence answer here, based strictly on the content.",
  "sources": ["Title of page 1", "Title of page 2"]
}}
"""

    raw = call_llm(prompt)
    return QAResponse(
        answer=f"LLM OUTPUT JSON:\n{raw}",
        sources=["Example source – Syllabus", "Example source – Final Project"],
    )
