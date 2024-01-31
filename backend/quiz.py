import openai
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()


def extract_q_and_a(question):
    # 질문을 라인으로 나눔
    lines = question.split("\n")

    # Q. A를 위한 변수 초기화
    q_part = ""
    a_part = ""

    # 라인을 반복하여 Q: 또는 질문: 및 A: 또는 답변: 찾기
    for line in lines:
        if line.startswith("Q:") or line.startswith("질문:"):
            q_part = line.strip()
        elif line.startswith("A:") or line.startswith("답변:"):
            a_part = line.strip()

        # 질문:이 존재할 때만 Q: 대체
        if "질문:" in q_part:
            q_part = q_part.replace("질문:", "Q:")

        # 답변:이 존재할 때만 A: 대체
        if "답변:" in a_part:
            a_part = a_part.replace("답변:", "A:")

        # 항상 Q:가 처음에 나오도록
        if not q_part.startswith("Q:"):
            q_part = f"Q: {q_part}"
    return q_part, a_part


# GPT-3.5-turbo를 사용하여 퀴즈 생성
def generate_quiz_question(context, model="gpt-3.5-turbo"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You have to make a quiz about computer security, and you have to make a question that can be answered in a sentence rather than a four-point first answer. And there should be no problems using pictures and tables. Q: A:",
                },
                {
                    "role": "user",
                    "content": f"Context: {context}\n\n---\n\n, 한국어로 대답해줘.",
                },
            ],
            temperature=0,
        )
        generated_question = response.choices[0].message.content

        # Q: or 질문: / A: or 답변:
        q_part, a_part = extract_q_and_a(generated_question)

        # Q가 처음에 나오게 하기 위해서
        return {"Q": q_part, "A": a_part}
    except Exception as e:
        print("Error occurred:", e)
        return {"Q": "I don't know", "A": "I don't know"}


# 피클 파일에서 로드한 데이터에서 랜덤한 문장을 선택하여 퀴즈 생성
def generate_random_quiz(df):
    # context = df.sample()["Text"].values[0]  # 예시로 랜덤하게 선택
    context = df.sample()["Tokens"].values[0]  # 예시로 랜덤하게 선택
    question = generate_quiz_question(context)
    return question
