from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_openai import OpenAI
from langchain.agents import AgentExecutor, Tool, create_self_ask_with_search_agent
from langchain import hub
from dotenv import load_dotenv
# import langchain
# langchain.debug = True
load_dotenv(override=True)

llm = OpenAI(temperature=0)
search = GoogleSerperAPIWrapper()
tools = [
    Tool(
        name="Intermediate Answer",
        func=search.run,
        description="useful for when you need to ask with search",
    )
]
prompt = hub.pull("hwchase17/self-ask-with-search")
agent = create_self_ask_with_search_agent(llm, tools, prompt)
self_ask_with_search = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
self_ask_with_search.invoke(
    {
        "input": "Where is the capital of a country that uses roses as its national flower?",
        # "input": "使用玫瑰作为国花的国家的首都是哪里?"
    }
)
