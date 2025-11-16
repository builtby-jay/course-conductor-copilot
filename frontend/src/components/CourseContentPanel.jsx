import React, { useState } from "react";
import { ingestPages } from "../api";

export default function CourseContentPanel() {
  const [pagesJson, setPagesJson] = useState(
    JSON.stringify(
      [
        {
          page_id: "final_project",
          title: "Final Project – Phishing Risk Assessment",
          content:
            "In this final project, you will act as a risk-management team working " +
            "to build organizational resilience for UVA Finance by focusing on phishing " +
            "risk at the employee level. You will design a Qualtrics survey, analyze a " +
            "blinded phishing-simulation dataset, and develop practical mitigations and " +
            "a targeted training program. Deliverables include a 5-page PDF report, a " +
            "PowerPoint deck, a 15-minute presentation, and peer evaluations."
        }
      ],
      null,
      2
    )
  );

  const [status, setStatus] = useState("");

  const handleIngest = async () => {
    try {
      const pages = JSON.parse(pagesJson);
      const res = await ingestPages(pages);
      setStatus(`Loaded ${res.num_pages} page(s).`);
    } catch (e) {
      console.error(e);
      setStatus("Error: invalid JSON or backend issue.");
    }
  };

  return (
    <section className="card">
      <h2>1. Course Content</h2>
      <p className="muted">
        Paste JSON describing course pages (<code>page_id</code>, <code>title</code>, <code>content</code>).
      </p>
      <textarea
        rows={18}
        value={pagesJson}
        onChange={(e) => setPagesJson(e.target.value)}
      />
      <button onClick={handleIngest}>Ingest pages</button>
      {status && <p className="status">{status}</p>}
    </section>
  );
}
