import httpx

VISION_URL = "http://vision-ai:8000/analyze"

async def run_pipeline(file):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            VISION_URL,
            files={"file": await file.read()}
        )

    architecture = response.json()

    return {
        "architecture": architecture,
        "status": "parsed"
    }
