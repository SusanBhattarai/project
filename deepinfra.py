import requests
import json

system_prompt = "You are a helpful assistant." # Yet to write a good specific prompt for this project.

def get_result(message):
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": message}
    ]
    
    data = {
        "model":"openai/gpt-oss-120b",
        "messages": messages,
        "stream":False,
    }
    try:
        req = requests.post("https://api.deepinfra.com/v1/openai/chat/completions", json=data)
        return json.loads(req.content)["choices"][0]["message"]["content"]
    except Exception as e:
        print("Error sending request to deepinfra. ", e)
    
