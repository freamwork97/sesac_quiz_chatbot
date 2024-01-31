from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import chatbot
from quiz import generate_random_quiz
from pydantic import BaseModel


class ChatInput(BaseModel):
    user_input: Optional[str] = None


# df = pd.read_pickle("../data/processed/test.pkl")
# df = pd.read_pickle("../data/processed/test2.pkl")
# df = pd.read_pickle("../data/processed/test3.pkl")
df = pd.read_pickle("../data/processed/test4.pkl")

QnA = {"Q": [], "A": []}

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 아래 함수가 핵심이다. 나머지 함수는 보조 목적으로 사용하는 함수다.
n = 0


@app.post("/chat")
async def chat(input_data: ChatInput):
    user_input = input_data.user_input

    if user_input is None:
        return {"message": "입력된 메시지가 없습니다."}

    response = chatbot.answer_question(user_input, df, debug=True)
    return {"User": user_input, "도봉이": response}


# 퀴즈 생성 API 엔드포인트
@app.get("/generate_quiz")
def generate_quiz():
    try:
        global n
        quiz = generate_random_quiz(df)
        QnA["Q"].append(quiz["Q"])
        QnA["A"].append(quiz["A"])
        n += 1
        print(QnA)
        return quiz
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")


# 퀴즈 이전 버튼 API 엔드포인트
@app.get("/devbutton")
def devbutton():
    try:
        global n
        n -= 1
        a = {"Q": QnA["Q"][n], "A": QnA["A"][n]}
        print(a)
        return a
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")


# 퀴즈 다음 버튼 API 엔드포인트
@app.get("/nextbutton")
def nextbutton():
    try:
        global n
        n += 1
        a = {"Q": QnA["Q"][n], "A": QnA["A"][n]}
        print(a)
        return a
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")
