from piper.voice import PiperVoice
import wave
import pygame

# Mude pro nome da sua voz baixada
MODEL_PATH = "audio/referencia_tsundere.wav"  # Ou a que você escolheu

voice = PiperVoice.load(MODEL_PATH)

def falar(texto):
    wav_bytes, sample_rate = voice.synthesize(texto)
    with wave.open("output/output.wav", "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(wav_bytes)
    
    pygame.mixer.init()
    pygame.mixer.music.load("output/output.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)