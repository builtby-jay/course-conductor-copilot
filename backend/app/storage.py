from typing import List, Dict

COURSE_PAGES: List[Dict] = []

def replace_pages(pages: List[Dict]):
    global COURSE_PAGES
    COURSE_PAGES = pages

def get_pages() -> List[Dict]:
    return COURSE_PAGES

def build_course_context() -> str:
    parts = []
    for page in COURSE_PAGES:
        header = f"### {page['title']} (id={page['page_id']})"
        parts.append(header)
        parts.append(page['content'])
    return "\n\n".join(parts)
