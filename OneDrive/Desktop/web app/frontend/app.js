import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [reportUrl, setReportUrl] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);
    formData.append("question", question);
    const res = await fetch("http://localhost:8000/analyze/", {
      method: "POST",
      body: formData,
    });
    const data = await res.json();
    setReportUrl(`http://localhost:8000/download/?report_path=${encodeURIComponent(data.report_path)}`);
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 600, margin: "auto", padding: 32 }}>
      <h1>Auto Statistical Report Generator</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} required />
        <br /><br />
        <input
          type="text"
          placeholder="Type your question (optional)"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          style={{ width: "100%" }}
        />
        <br /><br />
        <button type="submit" disabled={loading}>
          {loading ? "Generating..." : "Upload & Analyze"}
        </button>
      </form>
      {reportUrl && (
        <div style={{ marginTop: 24 }}>
          <a href={reportUrl} download>
            Download Report
          </a>
        </div>
      )}
    </div>
  );
}

export default App;
