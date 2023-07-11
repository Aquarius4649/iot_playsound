import RPi.GPIO as GPIO
import time
import pygame.mixer

GPIO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

pygame.mixer.init()
sound = pygame.mixer.Sound('./sound.wav')

def play_sound():
    if not pygame.mixer.get_busy():  # This line checks if there is a sound playing currently
        sound.play()
        time.sleep(3)  # Add the sleep here, after the sound is played

while True:
    if GPIO.input(GPIO_PIN) == GPIO.HIGH:
        print("反応あり")
        play_sound()  # call the function to play the sound

    else:
        print("反応なし")
        time.sleep(3)  # This sleep is to wait between checks of the GPIO pin
