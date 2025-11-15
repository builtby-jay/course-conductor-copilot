import React, { useState } from "react";
import { generateUpdates } from "../api";

export default function ChangePropagationPanel() {
  const [changeDescription, setChangeDescription] = useState("");
  const [audience, setAudience] = useState("students");
  const [channels, setChannels] = useState({
    announcement: true,
    email: true,
    policy: true,
  });
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const toggleChannel = (name) => {
    setChannels((prev) => ({ ...prev, [name]: !prev[name] }));
  };

  const handleGenerate = async () => {
    setLoading(true);
    setResult(null);
    try {
      const activeChannels = Object.entries(channels)
        .filter(([, v]) => v)
        .map(([k]) => k);
      const res = await generateUpdates(changeDescription, audience, activeChannels);
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
      <h2>2. Change Propagation</h2>
      <p className="muted">
        Describe changes (dates, policies, grading). Course Conductor drafts announcements,
        emails, and updated policy text.
      </p>

      <label>
        <span>Audience</span>
        <select value={audience} onChange={(e) => setAudience(e.target.value)}>
          <option value="students">Students</option>
          <option value="staff">Staff</option>
          <option value="all">All</option>
        </select>
      </label>

      <label>
        <span>Change description</span>
        <textarea
          rows={5}
          placeholder="Example: Move final project presentation from Dec 6 to Dec 8 and clarify 5-page report limit..."
          value={changeDescription}
          onChange={(e) => setChangeDescription(e.target.value)}
        />
      </label>

      <div className="channels">
        {["announcement", "email", "policy"].map((name) => (
          <label key={name}>
            <input
              type="checkbox"
              checked={channels[name]}
              onChange={() => toggleChannel(name)}
            />
            {name.charAt(0).toUpperCase() + name.slice(1)}
          </label>
        ))}
      </div>

      <button onClick={handleGenerate} disabled={loading}>
        {loading ? "Generating..." : "Generate drafts"}
      </button>

      {result && (
        <div className="results">
          {result.announcement && (
            <>
              <h3>Announcement Draft</h3>
              <pre>{result.announcement}</pre>
            </>
          )}
          {result.email && (
            <>
              <h3>Email Draft</h3>
              <pre>{result.email}</pre>
            </>
          )}
          {result.policy_snippet && (
            <>
              <h3>Policy Snippet</h3>
              <pre>{result.policy_snippet}</pre>
            </>
          )}
          {result.error && <p className="error">{result.error}</p>}
        </div>
      )}
    </section>
  );
}
