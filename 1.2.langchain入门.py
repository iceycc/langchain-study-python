import os

# 通过.env管理api_token
from dotenv import load_dotenv
load_dotenv(override=True)

from langchain.llms import HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="bigscience/bloom-1b7",
    task="text-generation",
    model_kwargs={"temperature": 0.1, "max_length": 64},
)
response = llm.predict("请给我的花店起个名")
print(response)
