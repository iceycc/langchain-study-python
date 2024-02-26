from langchain.prompts import PromptTemplate
# 通过.env管理api_token
from dotenv import load_dotenv
load_dotenv(override=True)

template = """\
你是业务咨询顾问。
你给一个销售{product}的电商公司，起一个好的名字？
"""
prompt1 = PromptTemplate.from_template(template)

print(prompt1.format(product="鲜花"))

prompt2 = PromptTemplate(
    input_variables=["product", "market"],
    template="你是业务咨询顾问。对于一个面向{market}市场的，专注于销售{product}的公司，你会推荐哪个名字？"
)
print(prompt2.format(product="鲜花", market="高端"))