import time
from fastapi import FastAPI

print("### main.py started ###")

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


# プロセスを生かす
while True:
    time.sleep(10)
