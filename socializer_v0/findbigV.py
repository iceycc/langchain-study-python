# 设置OpenAI API密钥
from dotenv import load_dotenv

load_dotenv(override=True)

# 导入所取的库
import re
from agents.weibo_agent import lookup_V
from tools.textgen_tool import generate_letter
from tools.general_tool import remove_non_chinese_fields
from tools.scraping_tool import get_data


def find_bigV(flower):
    print(flower)
    # 拿到UID
    # response_UID = lookup_V(flower_type=flower)

    # 抽取UID里面的数字
    # UID = re.findall(r'\d+', response_UID)[0]
    # print("这位鲜花大V的微博ID是", UID) # 6053338099
    UID = 6053338099
    # 根据UID爬取大V信息
    person_info = get_data(UID)
    # 移除无用的信息
    remove_non_chinese_fields(person_info)
    result = generate_letter(person_info)
    return result
