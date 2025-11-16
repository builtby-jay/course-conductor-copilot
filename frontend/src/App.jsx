import React from "react";
import CourseContentPanel from "./components/CourseContentPanel";
import ChangePropagationPanel from "./components/ChangePropagationPanel";
import QAPanel from "./components/QAPanel";
import "./styles.css";

export default function App() {
  return (
    <div className="app">
      <header className="app-header">
        <h1>Course Conductor – AI Ops Copilot</h1>
        <p>
          Streamlining the backbone of education by automating course communications and Q&amp;A.
        </p>
      </header>

      <main className="grid">
        <CourseContentPanel />
        <div className="stack">
          <ChangePropagationPanel />
          <QAPanel />
        </div>
      </main>
    </div>
  );
}
