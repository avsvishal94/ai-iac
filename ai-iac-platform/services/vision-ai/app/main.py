from fastapi import FastAPI, UploadFile
from .detector import detect_icons
from .graph_builder import build_graph
from .normalizer import normalize_graph

app = FastAPI(title="Vision AI Service")

@app.post("/analyze")
async def analyze_diagram(file: UploadFile):
    image_bytes = await file.read()
    detections = detect_icons(image_bytes)
    graph = build_graph(detections)
    return normalize_graph(graph)
