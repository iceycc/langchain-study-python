# 设置OpenAI API的密钥
from dotenv import load_dotenv

# 导入库
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentExecutor, create_react_agent
load_dotenv(override=True)

# 初始化模型和工具
llm = ChatOpenAI(temperature=0.0)
tools = load_tools(
    ["arxiv"],
)
prompt = hub.pull("hwchase17/react")
# 初始化链
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)



# 运行链
agent_executor.invoke(
    {
        "input": "What's the paper 1605.08386 about? use Chinese to explain it.",
    }
)
