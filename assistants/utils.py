import pygame
import random
from config.settings import PHRASE_AUDIO_DIR
import os

def psound():
    audio_choices = [f for f in os.listdir(PHRASE_AUDIO_DIR) if f.endswith('.wav')]
    audio_path = os.path.join(PHRASE_AUDIO_DIR, random.choice(audio_choices))
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue