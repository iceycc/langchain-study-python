# 项目：使用RAG模型进行检索
from dotenv import load_dotenv
from langchain.indexes import VectorstoreIndexCreator
# 导入文档加载器模块，并使用TextLoader来加载文本文件
from langchain_community.document_loaders import TextLoader

load_dotenv(override=True)

loader = TextLoader('./OneFlower/易速鲜花花语大全.txt', encoding='utf8')

# 使用VectorstoreIndexCreator来从加载器创建索引

index = VectorstoreIndexCreator().from_loaders([loader])

# 定义查询字符串, 使用创建的索引执行查询
query = "玫瑰花的花语是什么？"
result = index.query(query)
print(result)  # 打印查询结果
