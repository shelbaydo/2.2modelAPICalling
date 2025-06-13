import requests  # 导入requests库用于发送HTTP请求
import json  # 导入json库用于处理JSON数据

api_key = 'sk-9052aa7aa92f48089b15fd204ffb0279'  # DeepSeek API的密钥
url = "https://api.deepseek.com/chat/completions"  # DeepSeek API的端点URL

msg = [{"content":"You are a helpful assistant","role":"system"},  # 系统角色提示词
       {"content":"你好，今天星期几","role":"user"}]  # 用户输入的消息

payload = json.dumps({  # 构建请求体并转换为JSON字符串
  "messages": msg,  # 包含对话历史的消息列表
  "model": "deepseek-chat",  # 指定使用的模型名称
})

headers = {  # 设置HTTP请求头
  'Content-Type': 'application/json',  # 指定请求内容类型为JSON
  'Accept': 'application/json',  # 指定接受的响应类型为JSON
  'Authorization': f'Bearer {api_key}'  # 设置身份验证token
}

response = requests.request("POST", url, headers=headers, data=payload)  # 发送POST请求到API
print(type(response.text))  # 打印响应文本的类型
print(response.text)  # 打印API的响应内容