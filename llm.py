import ollama
import json
import os
from config import LLM_MODEL, SYSTEM_PROMPT, MEMORY_FILE

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memory(history):
    with open(MEMORY_FILE, "w") as f:
        json.dump(history[-20:], f)  # Últimas 20 trocas

def gerar_resposta(user_msg, history):
    context = "\n".join([f"User: {h['user']}\nRiko: {h['riko']}" for h in history[-10:]])
    prompt = f"{SYSTEM_PROMPT}\nContexto passado: {context}\nUser: {user_msg}\nRiko:"
    response = ollama.generate(model=LLM_MODEL, prompt=prompt)['response']
    history.append({"user": user_msg, "riko": response})
    save_memory(history)
    return response