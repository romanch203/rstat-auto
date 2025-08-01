# How to Run the Auto Statistical Report Web App

## Backend
1. Open a terminal in `backend/`.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key in `.env`.
4. Start the backend:
   ```
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

## Frontend
1. Open a terminal in `frontend/`.
2. Start a static server:
   ```
   npx serve .
   ```
3. Open `http://localhost:3000` (or the port shown) in your browser.

## Usage
- Upload a file (CSV, XLSX, DOCX).
- Optionally type a question.
- Download the generated report.

## AI Agent in VS Code
- Install: GitHub Copilot, ChatGPT, Python, Jupyter, Docker, REST Client extensions.
- (Optional) Ask for LangChain agent setup if needed.
