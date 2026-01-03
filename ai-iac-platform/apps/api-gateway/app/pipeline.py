import httpx

from generator.dispatcher import generate_terraform

VISION_AI_URL = "http://vision-ai:8000/analyze"


async def run_pipeline(file):
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            VISION_AI_URL,
            files={"file": await file.read()},
        )

    if response.status_code != 200:
        raise RuntimeError("Vision AI failed")

    vision_result = response.json()
    architecture = vision_result.get("architecture", vision_result)


    terraform_result = generate_terraform(architecture)

    return {
        "request_id": terraform_result["request_id"],
        "terraform_path": terraform_result["terraform_path"],
        "status": "terraform_generated",
    }
