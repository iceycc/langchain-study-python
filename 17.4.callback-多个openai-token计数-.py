from langchain_openai import OpenAI
from langchain_community.callbacks import get_openai_callback
import asyncio

from dotenv import load_dotenv

load_dotenv(override=True)
# 初始化大语言模型
llm = OpenAI(temperature=0.5, model_name="gpt-3.5-turbo-instruct")


# 进行更多的异步交互和token计数
async def additional_interactions():
    with get_openai_callback() as cb:
        await asyncio.gather(
            *[llm.agenerate(["我姐姐喜欢什么颜色的花？"]) for _ in range(3)]
        )
    print("\n另外的交互中使用的tokens:", cb.total_tokens)


# 运行异步函数
asyncio.run(additional_interactions())
