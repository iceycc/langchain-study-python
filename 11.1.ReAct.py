# 导入所需的库
from dotenv import load_dotenv
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain_openai import ChatOpenAI
import langchain
langchain.debug = True
# 在 serpapi.com 注册一个账号，并且拿到你的 SERPAPI_API_KEY
# pip install google-search-results # 安装这个库
load_dotenv(override=True)
llm = ChatOpenAI(temperature=0)

# 加载一些要使用的工具，包括 serpapi（这是调用 Google 搜索引擎的工具）以及 llm-math（这是通过 LLM 进行数学计算的工具）。
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# 初始化一个代理，这个代理是一个对话代理，它可以使用 LLM 进行对话。
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 通过对话代理进行对话
agent.run("目前市场上玫瑰花的平均价格是多少？如果我在此基础上加价15%卖出，应该如何定价？")