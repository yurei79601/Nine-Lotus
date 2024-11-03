import random
from typing import Dict

from fastapi import FastAPI
from questions import QUESTIONS_DICT

# 創建 FastAPI 應用
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}


# 定義一個接收 GET 請求的路由，並從 URL 中接收參數
@app.get("/questions/")
def get_questions(question_type: str) -> Dict[str, str]:
    return {
        "question_type": question_type,
        "question": random.choice(QUESTIONS_DICT[question_type]),
    }


@app.get("/confirm_symbols/")
def confirm_symbols(
    A: str,
    B: str,
    C: str,
    D: str,
) -> Dict[str, bool]:
    return {
        "A": A == "行",
        "B": B == "捨",
        "C": C == "忍",
        "D": D == "辦",
    }
