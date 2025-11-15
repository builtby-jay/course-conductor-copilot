from pydantic import BaseModel
from typing import List, Optional, Dict

class CoursePage(BaseModel):
    page_id: str
    title: str
    content: str

class IngestRequest(BaseModel):
    pages: List[CoursePage]

class ChangeRequest(BaseModel):
    change_description: str
    audience: str = "students"          # "students" | "staff" | "all"
    channels: List[str] = ["announcement", "email", "policy"]

class UpdateResponse(BaseModel):
    announcement: Optional[str] = None
    email: Optional[str] = None
    policy_snippet: Optional[str] = None

class QARequest(BaseModel):
    question: str

class QAResponse(BaseModel):
    answer: str
    sources: List[str]
