import time
from fastapi import FastAPI

print("### main.py started ###")

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


# 🔴 uvicornは一切使わない
while True:
    time.sleep(10)
