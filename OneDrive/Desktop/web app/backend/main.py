from fastapi import FastAPI, UploadFile, Form, File, Request
from typing import Optional
from fastapi.responses import FileResponse
from docx import Document
import openai, os
import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import process_file, summarize, generate_report, analyze_data, run_predictive, run_quality_control, run_machine_learning, run_inventory, run_workforce, run_cost, run_rd, run_environment

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/analyze/")
async def analyze_file(request: Request, file: Optional[UploadFile] = File(None), question: str = Form(""), analysis_type: str = Form("auto"), data: str = Form(None)):
    import traceback
    try:
        # If file is provided, use it. Otherwise, check for direct data entry.
        if file is not None:
            content = await file.read()
            data_obj = process_file(file.filename, content)
        elif data is not None:
            # Try to parse as JSON, else treat as plain text
            import json
            try:
                data_obj = pd.read_json(data)
            except Exception:
                try:
                    data_obj = pd.DataFrame(json.loads(data))
                except Exception:
                    data_obj = data  # treat as plain text
        else:
            return {"status": "error", "error": "No file or data provided."}
        # Flexible dispatcher for analysis type
        if analysis_type == "auto":
            if isinstance(data_obj, pd.DataFrame):
                stats = analyze_data(data_obj)
                summary = summarize(data_obj.to_string(), question)
                report_path = generate_report(summary, question, stats=stats, df=data_obj)
            elif isinstance(data_obj, str):
                summary = summarize(data_obj, question)
                report_path = generate_report(summary, question)
            else:
                summary = summarize(str(data_obj), question)
                report_path = generate_report(summary, question)
        elif analysis_type == "predictive":
            report_path = run_predictive(data_obj, question)
        elif analysis_type == "quality_control":
            report_path = run_quality_control(data_obj, question)
        elif analysis_type == "machine_learning":
            report_path = run_machine_learning(data_obj, question)
        elif analysis_type == "inventory":
            report_path = run_inventory(data_obj, question)
        elif analysis_type == "workforce":
            report_path = run_workforce(data_obj, question)
        elif analysis_type == "cost":
            report_path = run_cost(data_obj, question)
        elif analysis_type == "rd":
            report_path = run_rd(data_obj, question)
        elif analysis_type == "environment":
            report_path = run_environment(data_obj, question)
        else:
            return {"status": "error", "error": f"Unknown analysis_type: {analysis_type}"}
        return {"status": "success", "report_path": report_path}
    except Exception as e:
        tb = traceback.format_exc()
        return {"status": "error", "error": str(e), "traceback": tb}

@app.get("/download/")
def download_report(report_path: str):
    return FileResponse(report_path, media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

