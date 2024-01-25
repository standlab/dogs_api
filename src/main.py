from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def pingpong() -> dict[str, str]:
    return {"status": "ok", "content": "pong"}
