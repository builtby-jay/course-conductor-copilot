from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict, Any


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
COURSE_PAGES_FILE = DATA_DIR / "course_pages.json"


def load_course_pages() -> List[Dict[str, Any]]:
    """
    Load course pages from backend/data/course_pages.json.

    Returns a list of dicts like:
    { "page_id": "...", "title": "...", "content": "..." }

    If the file can't be read, falls back to a small built-in example.
    """
    if COURSE_PAGES_FILE.exists():
        try:
            text = COURSE_PAGES_FILE.read_text(encoding="utf-8")
            data = json.loads(text)
            if isinstance(data, list):
                print(f"[course_loader] Loaded {len(data)} course page(s) from {COURSE_PAGES_FILE}")
                return data
            else:
                print(f"[course_loader] WARNING: Expected a list in {COURSE_PAGES_FILE}, got {type(data)}")
        except Exception as e:
            print(f"[course_loader] ERROR reading {COURSE_PAGES_FILE}: {e}")

    print("[course_loader] Using built-in fallback course pages")
    return [
        {
            "page_id": "fallback_final_project",
            "title": "Final Project – Phishing Risk Assessment (Fallback)",
            "content": (
                "In this final project, students will act as a risk-management team focusing on phishing risk "
                "at the employee level. They will design a survey, analyze a blinded phishing simulation dataset, "
                "and produce a concise risk assessment report and presentation."
            ),
        }
    ]
