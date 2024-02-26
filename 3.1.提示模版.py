# 导入LangChain中的提示模板
from langchain.prompts import PromptTemplate
# 导入LangChain中的OpenAI模型接口
from langchain.llms import OpenAI

# 设置OpenAI API Key
import os

# 通过.env管理api_token
from dotenv import load_dotenv
load_dotenv(override=True)

# 导入LangChain中的提示模板
# 创建原始模板
template = """您是一位专业的鲜花店文案撰写员。\n
对于售价为 {price} 元的 {flower_name} ，您能提供一个吸引人的简短描述吗？
"""
# 根据原始模板创建LangChain提示模板
prompt = PromptTemplate.from_template(template)
# 打印LangChain提示模板的内容
print(prompt)

# 创建模型实例
model = OpenAI(model_name='text-davinci-003')
# 输入提示
input = prompt.format(flower_name=["玫瑰"], price='50')
# 得到模型的输出
output = model(input)
# 打印输出内容
print(output)