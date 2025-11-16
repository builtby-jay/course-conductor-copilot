# course-conductor-copilot
Orchestrating course communications so staff don’t have to.

cd "C:\Users\<user>\Documents\course-conductor-copilot\course-conductor-copilot\backend"

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1

$env:GEMINI_API_KEY = "gemini api key"
$env:GEMINI_MODEL   = "gemini-2.5-flash"

python -m uvicorn app.main:app --reload --port 8000

FRONTEND:

cd "C:\Users\<user>\Documents\course-conductor-copilot\course-conductor-copilot\frontend"
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
npm run dev