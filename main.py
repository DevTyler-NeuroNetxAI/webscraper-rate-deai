from fastapi import FastAPI, UploadFile, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import os

from scraper import start_scrape_job, get_job_status, list_results, get_result_file
from ai_text_tools import score_text, deai_text

app = FastAPI(title="Universal Educational Web Scraper & AI Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScrapeRequest(BaseModel):
    url: str
    use_js: bool = True
    doc_types: list = ["docx", "pdf", "csv", "xlsx", "pptx", "txt"]

@app.post("/scrape")
async def scrape(request: ScrapeRequest):
    job_id = await start_scrape_job(request.url, request.use_js, request.doc_types)
    return {"job_id": job_id}

@app.get("/status/{job_id}")
async def status(job_id: str):
    status, progress = get_job_status(job_id)
    return {"status": status, "progress": progress}

@app.get("/results/{domain}")
async def results(domain: str):
    return {"files": list_results(domain)}

@app.get("/download/{domain}/{filename}")
async def download(domain: str, filename: str):
    path = get_result_file(domain, filename)
    if not os.path.exists(path):
        return JSONResponse({"error": "File not found"}, status_code=404)
    return FileResponse(path, filename=filename)

@app.post("/score-text")
async def api_score_text(request: Request):
    data = await request.form()
    text = data.get("text", "")
    file = data.get("file", None)
    score = await score_text(text, file)
    return score

@app.post("/deai-text")
async def api_deai_text(request: Request):
    data = await request.form()
    text = data.get("text", "")
    file = data.get("file", None)
    level = int(data.get("level", 1))
    result = await deai_text(text, level, file)
    return result