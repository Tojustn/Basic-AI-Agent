import requests, json, ollama

client = ollama.Client()

def chat_response(message: str)-> str:
    model = "deepseek-r1"
    return  client.generate(model=model, prompt=message).response