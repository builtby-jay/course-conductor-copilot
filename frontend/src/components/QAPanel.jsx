import React, { useState } from "react";
import { askQuestion } from "../api";

export default function QAPanel() {
  const [question, setQuestion] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    setLoading(true);
    setResult(null);
    try {
      const res = await askQuestion(question);
      setResult(res);
    } catch (e) {
      console.error(e);
      setResult({ error: "Backend error" });
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="card">
      <h2>3. Course Q&amp;A</h2>
      <p className="muted">
        Ask logistics or policy questions. Answers are grounded in the ingested course content.
      </p>

      <label>
        <span>Question</span>
        <input
          type="text"
          placeholder="What is the final project about?"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />
      </label>

      <button onClick={handleAsk} disabled={loading}>
        {loading ? "Asking..." : "Ask"}
      </button>

      {result && (
        <div className="results">
          {result.answer && (
            <>
              <h3>Answer</h3>
              <pre>{result.answer}</pre>
            </>
          )}
          {result.sources && (
            <>
              <h4>Sources</h4>
              <ul>
                {result.sources.map((s) => (
                  <li key={s}>{s}</li>
                ))}
              </ul>
            </>
          )}
          {result.error && <p className="error">{result.error}</p>}
        </div>
      )}
    </section>
  );
}
