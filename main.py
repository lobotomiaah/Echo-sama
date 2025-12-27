import keyboard
from stt import gravar_e_transcrever
from llm import load_memory, gerar_resposta
from tts import falar

history = load_memory()
print("Waifu tsundere pronta! Segure Espaço para falar (Ctrl+C para sair).")

while True:
    keyboard.wait('space')  # Espera pressionar Espaço
    user_msg = gravar_e_transcrever()
    if user_msg.strip():
        resposta = gerar_resposta(user_msg, history)
        print("Riko:", resposta)
        falar(resposta)