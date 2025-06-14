import requests  # 导入requests库，用于发送HTTP请求
import json  # 导入json库，用于处理JSON数据
api_key = 'sk-9052aa7aa92f48089b15fd204ffb0279'  # 设置DeepSeek API的访问密钥
url = "https://api.deepseek.com/chat/completions"  # 设置DeepSeek API的端点URL
msg = [{"content":"You are a helpful assistant","role":"system"},{"content":"宋朝延续多少年,输出不超过50字","role":"user"}]  # 定义对话消息列表，包含系统提示和用户问题
payload = json.dumps({  # 构建API请求的负载数据并转换为JSON字符串
  "messages": msg,  # 设置对话消息
  "model": "deepseek-chat",  # 指定使用的AI模型
  "stream": True,  # 启用流式输出
  "max_tokens": 60,  # 设置最大生成token数
})
headers = {  # 设置HTTP请求头
  'Content-Type': 'application/json',  # 指定请求内容类型为JSON
  'Accept': 'application/json',  # 指定接受的响应类型为JSON
  "Authorization": f"Bearer {api_key}"  # 设置API认证信息
}
# 逐块处理响应
try:  # 开始异常处理
    response = requests.request("POST", url, headers=headers, data=payload, stream=True)  # 发送POST请求并获取响应
    response.raise_for_status()  # 检查HTTP响应状态，如果不是200则抛出异常
    for chunk in response.iter_lines():  # 逐行读取流式响应
        if chunk:  # 如果数据块不为空
            decoded_chunk = chunk.decode('utf-8').strip()  # 将字节流解码为字符串并去除首尾空白
            print(decoded_chunk)  # 打印解码后的数据块
except requests.exceptions.RequestException as e:  # 捕获请求过程中的异常
    print(f"\n请求失败: {e}")  # 打印错误信息
