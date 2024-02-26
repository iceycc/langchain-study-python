import openai

# 通过.env管理api_token
from dotenv import load_dotenv
load_dotenv(override=True)

# response = openai.Completion.create(
#     model="text-davinci-003",
#     temperature=0.5,
#     max_tokens=100,
#     prompt="请给我的花店起个名")
#
# print(response.choices[0].text.strip())
# 百花园、绽放花店、芳草地、芬芳花园、芳花坊、芳草花店、芳花苑、芳草园、芳草轩、芳花轩、

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a creative AI."},
        {"role": "user", "content": "请给我的花店起个名"},
    ],
  temperature=0.8,
  max_tokens=60
)
print(response['choices'][0]['message']['content'])
