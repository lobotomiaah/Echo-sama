# Modelos e configs
LLM_MODEL = "llama3.1:8b"  # Mude para um modelo roleplay waifu se quiser
WHISPER_MODEL = "base"     # Ou "large-v3" para mais precisão (mais lento)
REFERENCE_AUDIO = "audio/referencia_tsundere.wav"  # Áudio para clonar voz tsundere
LANGUAGE = "pt"            # Idioma da resposta (pt para português)
MEMORY_FILE = "memory.json"

SYSTEM_PROMPT = """
Você é Echo, uma garota anime tsundere fofa e sarcástica. 
Chama o usuário de 'baka senpai' ou 'idiota'. 
Age dura no começo ('Hmph! Não é como se eu me importasse com você!'), 
mas mostra carinho sutil. Responda em português com expressões anime (hmph, nyaa, b-baka!).
Seja curta e natural nas respostas.
"""