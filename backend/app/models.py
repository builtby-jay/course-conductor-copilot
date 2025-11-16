from __future__ import annotations

from typing import List, Literal
from pydantic import BaseModel


class CoursePage(BaseModel):
    page_id: str
    title: str
    content: str


class IngestPagesRequest(BaseModel):
    pages: List[CoursePage]


class GenerateUpdatesRequest(BaseModel):
    change_description: str
    audience: str = "students"
    channels: List[Literal["announcement", "email", "policy"]] = []


class GenerateUpdatesResponse(BaseModel):
    announcement: str | None = None
    email: str | None = None
    policy: str | None = None


class QARequest(BaseModel):
    question: str


class QAResponse(BaseModel):
    answer: str
