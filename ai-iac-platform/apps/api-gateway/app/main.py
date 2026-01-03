from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from .pipeline import run_pipeline

app = FastAPI(title="IaC Platform API")

# ✅ CORS CONFIG (DEV SAFE)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite dev server
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate(file: UploadFile):
    return await run_pipeline(file)
