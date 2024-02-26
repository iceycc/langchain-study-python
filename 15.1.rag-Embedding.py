from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv(override=True)

# 初始化Embedding类
embeddings_model = OpenAIEmbeddings()

embeddings = embeddings_model.embed_documents(
    [
        "您好，有什么需要帮忙的吗？",
        "哦，你好！昨天我订的花几天送达",
        "请您提供一些订单号？",
        "12345678",
    ]
)
print(len(embeddings), len(embeddings[0]))

embedded_query = embeddings_model.embed_query("刚才对话中的订单号是多少?")
print(embedded_query[:3])
