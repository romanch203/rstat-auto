# RStat Auto

An RStudio-based automation system that:
- Accepts `.csv`, `.xlsx`, `.pdf`, `.docx`, and `.txt`
- Extracts and analyzes statistical data
- Creates plots, summaries, and interpretations
- Generates full PDF reports
- Provides a REST API

## Run locally in RStudio
1. Open `main.R`
2. Install required packages
3. Run

## Run via Docker
```bash
docker build -t rstat_auto .
docker run -p 8000:8000 rstat_auto
```

## API Endpoint
POST `/analyze` with `multipart/form-data` containing the file.
Returns base64-encoded PDF report.
