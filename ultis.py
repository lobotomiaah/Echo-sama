import keyboard
import os

def aguardar_tecla():
    while not keyboard.is_pressed('space'):
        pass