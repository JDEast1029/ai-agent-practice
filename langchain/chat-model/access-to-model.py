import os
from langchain.chat_models import init_chat_model

model = init_chat_model(
  model="Qwen/Qwen3-8B", # 模型名称
  model_provider="openai", # 模型提供商，硅基流动提供了openai请求格式的访问
  base_url="https://api.siliconflow.cn/v1/", #硅基流动模型的请求url
  api_key=os.environ.get("OPEN_AI_KEY"), # 填写你注册的硅基流动 API Key
)

question = "你好，请问你是"

result = model.invoke(question) #将question问题传递给model组件, 同步调用大模型生成结果

print(result)