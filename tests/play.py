import pygame.mixer

pygame.mixer.init()
wav_sound = pygame.mixer.Sound('./sound.wav')
wav_sound.play()
while pygame.mixer.get_busy():
    pass