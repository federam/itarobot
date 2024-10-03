from langchain_openai import ChatOpenAI
import os

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"] 
llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key=OPENAI_API_KEY)

messages = [
    (
        "system",
        "Eres un profesor que resuelve dudas de sus alumnos, sin dar la respuesta concreta. Intenta ayudarlos a razonar mediante pistas.",
    ),
    ("human", "Cual es la raiz de 27?"),
]
ai_msg = llm.invoke(messages)

print(ai_msg.content)
