# Course Conductor – Backend

This is the FastAPI backend for **Course Conductor**, an AI ops copilot that
ingests course content and uses OpenAI's API to generate course communications
and answer logistics questions.

## Tech stack

- Python 3.10+
- FastAPI
- Uvicorn
- OpenAI Python SDK

## Setup

1. **Create a virtual environment and install dependencies**

```bash
cd backend
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
