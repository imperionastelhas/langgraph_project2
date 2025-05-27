import requests

response = requests.post("http://localhost:2024/agent/invoke", json={
    "messages": [
        {"type": "human", "content": "What is the weather in Rio de Janeiro?"}
    ]
})

print(response.status_code)
print(response.json())

