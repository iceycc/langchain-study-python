from langchain_community.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory

from dotenv import load_dotenv

load_dotenv(override=True)
# 初始化大语言模型
llm = OpenAI(
    temperature=0.5,
    model_name="gpt-3.5-turbo-instruct"
)

# 初始化对话链
conversation = ConversationChain(
    llm=llm,
    memory=ConversationBufferWindowMemory(k=1),
)

# 打印对话的模板
# print(conversation.prompt.template)

# 第一天对话
# 回合 1
result = conversation("我姐姐明天要过生日，我想送她一束生日花束。")
print('第一次', result)

# 回合 2
result = conversation("她喜欢粉色玫瑰，颜色是粉色的。")
print('第二次', result)


# 回合3 （第二天的对话）
result = conversation("我又来了，还记得我昨天为什么要来买花吗？")
print('第三次', result)

