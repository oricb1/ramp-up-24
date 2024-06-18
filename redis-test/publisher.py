from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis

app = FastAPI()

# Connect to Redis
r = redis.Redis(host='redis', port=6379, decode_responses=True)

class Message(BaseModel):
    message: str

@app.post("/publish")
async def publish_message(msg: Message):
    if not msg.message:
        raise HTTPException(status_code=400, detail="No message provided")
    
    r.publish('my_channel', msg.message)
    return {"status": "Message published"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)