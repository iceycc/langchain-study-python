from socializer_v0.tools.search_tool import get_UID
# 导入所需的库
from langchain import hub
from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool,create_react_agent, AgentExecutor

from langchain.agents import AgentType


# 通过LangChain代理找到UID的函数
def lookup_V(flower_type: str):
    # 初始化大模型
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # 寻找UID的模板
    template = """given the {flower} I want you to get a related 微博 UID.
                  Your answer should contain only a UID.
                  The URL always starts with https://weibo.com/u/
                  for example, if https://weibo.com/u/1669879400 is her 微博, then 1669879400 is her UID
                  This is only the example don't give me this, but the actual UID"""
    # 完整的提示模板
    prompt_template = PromptTemplate(
        input_variables=["flower"], template=template
    )

    # 代理的工具
    tools = [
        Tool(
            name="Crawl Google for 微博 page",
            func=get_UID,
            description="useful for when you need get the 微博 UID",
        )
    ]

    prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(llm, tools, prompt)
    # 初始化代理
    agent_a = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # 返回找到的UID
    ID = agent_a.invoke({
        "input": prompt_template.format_prompt(flower=flower_type),
    })

    return ID
