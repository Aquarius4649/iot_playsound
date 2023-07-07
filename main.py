import RPi.GPIO as GPIO
import time
import pygame.mixer

GPIO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN,GPIO.IN)

pygame.mixer.init()  # It is generally better to initialize pygame.mixer once rather than in a loop
sound = pygame.mixer.Sound('./sound.wav')

def play_sound():
    if not pygame.mixer.get_busy():  # This line checks if there is a sound playing currently
        sound.play()

while True:
    if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
        print("反応あり")
        play_sound()  # call the function to play the sound
        time.sleep(1)

    else:
        print("反応なし")
        time.sleep(1)
