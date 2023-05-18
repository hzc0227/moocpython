# -*- coding = utf-8 -*-
# @author:   hanzhihchao7
# @date:     2023/2/13 9:57
# @File:     ChatGPT.py
# @Software: PyCharm


# 设置 API Key
import openai

openai.api_key = "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"

# 设置请求参数

model_engine = "text-davinci-002"

prompt = "python的应用领域"

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=3000,
    n=2,
    stop=None,
    temperature=0.5)

# 获取 ChatGPT 的回复
message = completions.choices[0].text

print(message)
