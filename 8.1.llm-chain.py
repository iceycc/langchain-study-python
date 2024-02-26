# 导入所需的库
from langchain_community.llms import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
# 通过.env管理api_token
from dotenv import load_dotenv
load_dotenv(override=True)

# 原始字符串模板
template = "{flower}的花语是?"
# 创建模型实例
llm = OpenAI(temperature=0)
# 创建LLMChain
llm_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(template))
# 调用LLMChain，返回结果
# result = llm_chain("玫瑰")
input_list = [ {"flower": "玫瑰",'season': "夏季"}, {"flower": "百合",'season': "春季"}, {"flower": "郁金香",'season': "秋季"}]
result = llm_chain.apply(input_list)
print(result)
