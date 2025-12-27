import speech_recognition as sr
import pyttsx3
import json
import os
import ollama

# ======================
# CONFIGURAÇÃO
# ======================
MODEL_NAME = "mistral"
MEMORY_FILE = "memory.json"

SYSTEM_PROMPT = """
Você é uma assistente virtual tsundere.
Você fala português brasileiro.
Você ajuda, mas finge que não se importa.
Você pode ser sarcástica, mas não ofensiva.
Você lembra informações importantes do usuário.
"""

# ======================
# MEMÓRIA
# ======================
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"name": None, "facts": []}

def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=4)

memory = load_memory()

def memory_context():
    text = ""
    if memory["name"]:
        text += f"O nome do usuário é {memory['name']}.\n"
    if memory["facts"]:
        text += "Informações importantes sobre o usuário:\n"
        for fact in memory["facts"]:
            text += f"- {fact}\n"
    return text

# ======================
# VOZ
# ======================
tts = pyttsx3.init()
tts.setProperty("rate", 180)

def speak(text):
    print("🤖 IA:", text)
    tts.say(text)
    tts.runAndWait()

# ======================
# OUVIR MICROFONE
# ======================
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Fale algo...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="pt-BR")
        print("🗣 Você:", text)
        return text
    except:
        return ""

# ======================
# OLLAMA
# ======================
def ask_ollama(user_text):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT + "\n" + memory_context()},
        {"role": "user", "content": user_text}
    ]

    response = ollama.chat(
        model=MODEL_NAME,
        messages=messages
    )

    return response["message"]["content"]

# ======================
# MEMORIZAR COISAS
# ======================
def check_memory(user_text):
    text = user_text.lower()

    if "meu nome é" in text:
        name = user_text.split("meu nome é")[-1].strip()
        memory["name"] = name
        save_memory(memory)
        speak(f"Hmpf… então seu nome é {name}. Vou lembrar disso.")

    if "lembra que" in text:
        fact = user_text.split("lembra que")[-1].strip()
        memory["facts"].append(fact)
        save_memory(memory)
        speak("Tsc… tá bom, vou guardar isso.")

# ======================
# LOOP PRINCIPAL
# ======================
speak("Tsc… ligou o sistema. Não pense que eu estava esperando.")

while True:
    user_text = listen()

    if not user_text:
        speak("Hã? Fala direito, baka.")
        continue

    if "sair" in user_text.lower():
        speak("T-tanto faz… até mais.")
        break

    check_memory(user_text)

    reply = ask_ollama(user_text)
    speak(reply)
