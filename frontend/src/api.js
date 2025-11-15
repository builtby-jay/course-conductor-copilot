const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

export async function ingestPages(pages) {
  const res = await fetch(`${API_BASE}/api/ingest-pages`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ pages }),
  });
  return res.json();
}

export async function generateUpdates(changeDescription, audience, channels) {
  const res = await fetch(`${API_BASE}/api/generate-updates`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ change_description: changeDescription, audience, channels }),
  });
  return res.json();
}

export async function askQuestion(question) {
  const res = await fetch(`${API_BASE}/api/qa`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question }),
  });
  return res.json();
}
