# 设置环境变量和API密钥
from dotenv import load_dotenv
load_dotenv(override=True)

# 创建聊天模型
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature=0)

# 设定 AI 的角色和目标
role_template = "请你模拟三位出色、逻辑性强的专家合作回答一个问题。"

# CoT 的关键部分，AI 解释推理过程，并加入一些先前的对话示例（Few-Shot Learning）
cot_template = """
每个人都详细地解释他们的思考过程，考虑到其他人之前的解释，并公开承认错误。
在每一步，只要可能，每位专家都会在其他人的思考基础上进行完善和建设，并承认他们的贡献。
他们继续，直到对问题有一个明确的答案。为了清晰起见，您的整个回应应该是一个 Markdown 表格。

问题是
"""
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
system_prompt_role = SystemMessagePromptTemplate.from_template(role_template)
system_prompt_cot = SystemMessagePromptTemplate.from_template(cot_template)

# 用户的询问
human_template = "{human_input}"
human_prompt = HumanMessagePromptTemplate.from_template(human_template)

# 将以上所有信息结合为一个聊天提示
chat_prompt = ChatPromptTemplate.from_messages([system_prompt_role, system_prompt_cot, human_prompt])

prompt = chat_prompt.format_prompt(human_input="我想为我的女朋友购买一些花。她喜欢粉色和紫色。你有什么建议吗?").to_messages()

# 接收用户的询问，返回回答结果
response = llm(prompt)
print(response)