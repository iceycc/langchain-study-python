from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_async_playwright_browser
from langchain.agents import initialize_agent, AgentType
from langchain_openai.chat_models import ChatOpenAI
import asyncio

from dotenv import load_dotenv

load_dotenv(override=True)

# 使用Playwright上下文管理器
async_browser = create_async_playwright_browser()
toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
tools = toolkit.get_tools()
print(tools)

# LLM不稳定，对于这个任务，可能要多跑几次才能得到正确结果
llm = ChatOpenAI(temperature=0.5)

agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)


async def main():
    response = await agent_chain.arun("What are the headers on python.langchain.com?")
    print(response)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
