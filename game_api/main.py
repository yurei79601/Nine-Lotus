import random

from fastapi import FastAPI
from questions import QUESTIONS_DICT

# 創建 FastAPI 應用
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}


# 定義一個接收 GET 請求的路由，並從 URL 中接收參數
@app.get("/questions/")
def read_item(question_type: str):
    return {
        "question_type": question_type,
        "question": random.choice(QUESTIONS_DICT[question_type]),
    }
