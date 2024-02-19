# Contents of app/main.py

from fastapi import FastAPI, Response
from .api.sql_generator import router as sql_generation_router
import asyncio
app = FastAPI()
from fastapi.responses import StreamingResponse


@app.get("/stream-text/")
async def stream_text():
    text = "This is a sample text to stream word by word."
    words = text.split()

    async def event_stream():
        for word in words:
            yield f"data: {word}\n\n"
            await asyncio.sleep(1)  # Wait for 1 second before sending the next word

    return StreamingResponse(event_stream(), media_type="text/event-stream")

app.include_router(sql_generation_router)
