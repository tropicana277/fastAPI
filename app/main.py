from fastapi import FastAPI, HTTPException
from datetime import datetime, timezone
from .dynamodb import get_table
from .models import UserCreate


app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/users")
def create_user(user: UserCreate):
    table = get_table()  # ← ここで初めて DynamoDB に接続
    item = {**user.model_dump(), "created_at": datetime.now(timezone.utc).isoformat()}
    table.put_item(Item=item)
    return item


@app.get("/users/{user_id}")
def get_user(user_id: str):
    table = get_table()
    res = table.get_item(Key={"user_id": user_id})
    if "Item" not in res:
        raise HTTPException(status_code=404, detail="User not found")
    return res["Item"]


@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    table = get_table()
    table.delete_item(Key={"user_id": user_id})
    return {"message": "deleted"}
