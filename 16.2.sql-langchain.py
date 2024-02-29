# 导入langchain的实用工具和相关的模块
# https://python.langchain.com/docs/use_cases/sql/agents
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits import create_sql_agent
# from langchain_experimental.sql import SQLDatabaseChain
from dotenv import load_dotenv
load_dotenv(override=True)
# 连接到FlowerShop数据库（之前我们使用的是Chinook.db）
db = SQLDatabase.from_uri("sqlite:///FlowerShop.db")
# print(db.run("SELECT * FROM Flowers"))
# 创建OpenAI的低级语言模型（LLM）实例，这里我们设置温度为0，意味着模型输出会更加确定性
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 创建SQL数据库链实例，它允许我们使用LLM来查询SQL数据库
# db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)
# 运行与鲜花运营相关的问题
response = agent_executor.invoke("哪种鲜花的存货数量最少？")
print(response)

response = agent_executor.invoke("哪种鲜花的存货数量最少？")
print(response)

response = agent_executor.invoke("平均销售价格是多少？")
print(response)

response = agent_executor.invoke("从法国进口的鲜花有多少种？")
print(response)

response = agent_executor.invoke("哪种鲜花的销售量最高？")
print(response)