import os

# 通过.env管理api_token
from dotenv import load_dotenv
load_dotenv(override=True)
## text模型
# from langchain.llms import OpenAI
# llm = OpenAI(
#     model="text-davinci-003",
#     temperature=0.8,
#     max_tokens=60,)
# response = llm.predict("请给我的花店起个名")
# print(response)

# chat模型
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(model="gpt-3.5-turbo",
                  temperature=0.8,
                  request_timeout=120,
                  max_tokens=60)
from langchain.schema import (
    HumanMessage,
    SystemMessage
)

messages = [
    SystemMessage(content="你是一个很棒的智能助手"),
    HumanMessage(content="请给我的花店起个名")
]
response = chat(messages)
print(response)
