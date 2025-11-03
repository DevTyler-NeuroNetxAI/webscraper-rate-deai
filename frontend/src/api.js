export async function startScrape(url, docTypes) {
  const resp = await fetch("http://localhost:8000/scrape", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({url, doc_types: docTypes})
  });
  if (!resp.ok) throw new Error("Backend error");
  return await resp.json();
}

export async function getStatus(jobId) {
  const resp = await fetch(`http://localhost:8000/status/${jobId}`);
  if (!resp.ok) throw new Error("Backend error");
  return await resp.json();
}

export async function getResults(domain) {
  const resp = await fetch(`http://localhost:8000/results/${domain}`);
  if (!resp.ok) throw new Error("Backend error");
  return await resp.json();
}

export async function downloadFile(domain, filename) {
  window.open(`http://localhost:8000/download/${domain}/${filename}`, "_blank");
}

export async function scoreText(text) {
  const form = new FormData();
  form.append("text", text);
  const resp = await fetch("http://localhost:8000/score-text", { method: "POST", body: form });
  if (!resp.ok) throw new Error("Backend error");
  return await resp.json();
}

export async function deaiText(text, level) {
  const form = new FormData();
  form.append("text", text);
  form.append("level", level);
  const resp = await fetch("http://localhost:8000/deai-text", { method: "POST", body: form });
  if (!resp.ok) throw new Error("Backend error");
  return await resp.json();
}