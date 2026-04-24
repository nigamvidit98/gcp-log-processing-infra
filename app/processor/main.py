from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/logs")
async def receive_logs(request: Request):
    data = await request.body()
    print(f"Received log: {data.decode()}")
    return {"status": "ok"}

@app.get("/")
def health():
    return {"status": "running"}
