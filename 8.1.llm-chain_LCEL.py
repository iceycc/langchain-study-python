# 导入所需的库
from langchain_community.llms import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
# 通过.env管理api_token
from dotenv import load_dotenv

load_dotenv(override=True)

# 原始字符串模板
template = "{flower}的花语是?"
# 创建提示模板
prompt = PromptTemplate.from_template(template)
# 创建模型实例
llm = OpenAI(temperature=0)
# 创建解析器
out_parser = StrOutputParser()
# 创建LLMChain
chain = prompt | llm | out_parser
# 调用LLMChain，返回结果
# result = llm_chain("玫瑰")
input_list = [{"flower": "玫瑰", 'season': "夏季"}, {"flower": "百合", 'season': "春季"},
              {"flower": "郁金香", 'season': "秋季"}]

# result = chain.invoke(input_list[0])
result = chain.batch(input_list)
print(result)
