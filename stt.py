from faster_whisper import WhisperModel
import wave
import numpy as np
import sounddevice as sd
from pynput import keyboard as pynput_keyboard
import torch   # <--- ESSA LINHA ESTAVA FALTANDO!!!
from config import WHISPER_MODEL

model = WhisperModel(WHISPER_MODEL, device="cuda" if torch.cuda.is_available() else "cpu")
listener = None
is_recording = False

def on_press(key):
    global is_recording
    try:
        if key == pynput_keyboard.Key.space:
            is_recording = True
            print("🎤 Gravando... (solte Espaço para parar)")
    except:
        pass

def on_release(key):
    global is_recording
    try:
        if key == pynput_keyboard.Key.space and is_recording:
            is_recording = False
            print("⏹️ Processando áudio...")
            return False  # Para o listener temporariamente
    except:
        pass

def gravar_e_transcrever():
    global listener
    
    # Inicia listener de teclado
    listener = pynput_keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    
    print("Segure Espaço para falar...")
    
    # Espera começar a gravar
    while not is_recording:
        pass
    
    samplerate = 16000
    audio_frames = []
    
    with sd.RawInputStream(samplerate=samplerate, blocksize=1024, dtype='int16', channels=1) as stream:
        while is_recording:
            data, _ = stream.read(1024)
            audio_frames.append(data)
    
    # Para o listener
    listener.stop()
    
    if not audio_frames:
        return ""
    
    audio = np.concatenate(audio_frames, axis=0)
    with wave.open("audio/temp.wav", "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio.tobytes())
    
    segments, _ = model.transcribe("audio/temp.wav", language="pt")
    texto = " ".join(seg.text for seg in segments).strip()
    print("Você:", texto)
    return texto