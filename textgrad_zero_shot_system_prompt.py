# -*- coding: utf-8 -*-
"""textgrad-zero-shot-system-prompt.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PB4Y5LXNz19vHlFhoBlz86VChVM0Nsqf

## 使用 Textgrad 最佳化 system prompt 🏆



這個 Notebook 使用 https://textgrad.com/ 進行 system prompt 的最佳化

* 輸入你的任務描述
* 就能產出很厲害 zero-shot prompt
* 用在沒有標準答案的場景，採用 LLM 自動評估

作者和演講投影片: ihower https://ihower.tw/blog/archives/12444

### 流程

1. 使用 o1-preview 合成訓練問題
2. 使用 gpt-4o 進行 textgrad 最佳化，採用 LLM-as-a-judge 自動化評估
3. 產生適合 gpt-4o-mini 的 system prompt

成本: 最佳化迭代大約要花5分鐘，耗費 USD 0.8 美金 (10個訓練範例)

## 0. 設定 OpenAI API key

請點 google colab 左邊側欄的鑰匙符號，新增密鑰，名稱是 openai_api_key，值就填 API key
"""

from google.colab import userdata
import os
import json

os.environ["OPENAI_API_KEY"] = userdata.get('openai_api_key')

"""## 1. 設定參數"""

synthetic_model = "o1-preview" # 合成訓練問題的模型，若你沒有 o1 權限，請改用 gpt-4o"
generation_model = "gpt-4o" # 合成 prompt 的模型
prediction_model = "gpt-4o-mini" # 用來執行 prompt 的模型

task_description = "根據用戶輸入的專業領域，條列其中的關鍵知識重點" # 任務描述，請修改成你的任務

questions_num = 10  # 要合成多少訓練資料，跟花費的 API 成本有關，建議不要再少了，會 overfitting

# 用來評估答案好不好的 prompt，可以改，但請保留 [question_string] 字串
eval_prompt_template = """Here's a question: [question_string].
Evaluate any given answer to this question, be smart, logical, and very critical.
Just provide concise feedback."""

"""## 2. 合成最佳化需要的 dataset

"""

synthetic_prompt = f"""You are tasked with creating a test dataset for an AI question-answering system. Your goal is to generate {questions_num} example questions based on a given task description. These questions should range from simple to complex, with the more difficult questions requiring reasoning and presenting a significant challenge.
Here are the guidelines for generating the questions:

Start with simple, straightforward questions and gradually increase the complexity.
Ensure that the more difficult questions require multi-step reasoning or in-depth knowledge.
Include a variety of question types (e.g., factual, analytical, hypothetical) relevant to the task description.
Ensure that all questions are directly related to the provided task description.

The task description you should base your questions on is as follows:
<task_description>
{task_description}
</task_description>

Please generate {questions_num} example questions based on this task description. Format your output as a JSON array of objects, where each object contains a 'question' key with the question text as its value, and an 'answer' key with the answer text as its value. The output should look like this:
[
{{"question": "Question 1 text here", "answer": "Answer 1 text here"}},
{{"question": "Question 2 text here", "answer": "Answer 2 text here"}},
...
]

Remember to increase the difficulty and complexity of the questions as you progress through the examples. The final few questions should be particularly challenging, requiring complex reasoning and demonstrating a high level of difficulty."""

!pip install litellm

from litellm import completion

messages = [
    { "content": synthetic_prompt, "role": "user"}
]

if not synthetic_model.startswith('o1'):
  response = completion(model=synthetic_model, messages=messages, response_format={ "type": "json_object" })
else:
  # o1 目前還不支援 json mode
  response = completion(model=synthetic_model, messages=messages)

response = response.choices[0].message.content
dataset = json.loads(response)

dataset

"""## 3. 使用 Textgrad 最佳化 system prompt"""

!pip install textgrad

import textgrad as tg
from textgrad.tasks import load_task

llm_engine = tg.get_engine(prediction_model, override=True )
tg.set_backward_engine(generation_model, override=True )

system_prompt = tg.Variable("You are a concise LLM.",
                            requires_grad=True,
                            role_description="system prompt to guide the LLM's reasoning strategy for accurate responses")

model = tg.BlackboxLLM(llm_engine, system_prompt=system_prompt)
optimizer = tg.TGD(parameters=list(model.parameters()))

# 開始跑最佳化迭代
for data in dataset:
    question_string = data["question"]
    question = tg.Variable(question_string, role_description="question to the LLM", requires_grad=False)

    optimizer.zero_grad()
    prediction = model(question)
    prediction.set_role_description("concise and accurate answer to the question")

    evaluation_instruction = eval_prompt_template.replace( '[question_string]', question_string)
    loss_fn = tg.TextLoss(evaluation_instruction)
    loss = loss_fn(prediction)

    loss.backward()
    optimizer.step()

# 輸出最終的 system prompt 結果
print(system_prompt.value)

"""以下是這個 system prompt 中文翻譯供對照: https://chatgpt.com/share/66ea86da-4040-8008-a2f9-cc5806fa5f05"""