from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

from routes import backend, connect

app = FastAPI()

app.include_router(backend.router)
app.include_router(connect.router)

@app.get("/")
async def read_root():
    return JSONResponse(content={"message": "I'm alive"}, status_code=200)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)