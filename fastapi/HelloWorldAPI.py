from fastapi import FastAPI

app = FastAPI()

@app.get("/{input}")
async def readName(input : str):
    return {"message": f"Hello {input}"}
