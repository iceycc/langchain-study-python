from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser

# 载入 apikey
from dotenv import load_dotenv

load_dotenv(override=True)

# 1、创建提示模板
prompt = PromptTemplate.from_template("生产一个关于{flower}的故事。")

# 2、创建模型实例
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5, max_tokens=2000)

# 3、创建解析器
out_parser = StrOutputParser()

# 4、创建 chain
chain = prompt | llm | out_parser

# 准备数据
input_list = [{"flower": "玫瑰"}, {"flower": "百合"}, {"flower": "郁金香"}]
# 调用 chain
# result = chain.invoke(input_list[0])
# print(result)

# results = chain.batch(input_list)
# print(results)

#
for chunk in chain.stream(input_list[2]):
    print(chunk, end="", flush=True) # end="" 保持原样输出，flush=True 立即输出
