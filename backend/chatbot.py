import openai
from dotenv import load_dotenv
from scipy.spatial.distance import cosine
import os
from openai import OpenAI

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()


def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding


def create_context(question, df, max_len=3000):
    q_embedding = (
        client.embeddings.create(input=question, model="text-embedding-ada-002")
        .data[0]
        .embedding
    )
    df["distances"] = df["embedding"].apply(lambda x: cosine(q_embedding, x))
    cur_len = 0
    context_parts = []
    for _, row in df.sort_values("distances", ascending=True).iterrows():
        cur_len += row["n_tokens"] + 4
        if cur_len > max_len:
            break
        # context_parts.append(row["Text"])
        context_parts.append(row["Tokens"])
    return "\n\n===\n\n".join(context_parts)


def answer_question(question, df, max_len=3000, debug=False):
    context = create_context(question, df, max_len=max_len)
    if debug:
        print("Context:\n" + context)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Answer the question based on the context below, try to explain anyway but if the question can't be answered based on the context, say \"I don't know\"\n\n",
                },
                {
                    "role": "user",
                    "content": f"Context: {context}\n\n---\n\n Question: {question}, 한국어로 번역해서 대답해줘.",
                },
            ],
            temperature=0,
        )
        return response.choices[0].message.content
    except Exception as e:
        print("Error occurred:", e)
        return "I don't know"
