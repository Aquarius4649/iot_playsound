import RPi.GPIO as GPIO
import time
import pygame.mixer
import random

GPIO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)

num = 1
pygame.mixer.init()
file_name = "./" + str(num) + ".wav"
pygame.mixer.music.load(file_name)

while True:
    if GPIO.input(GPIO_PIN) == GPIO.HIGH:
        print("反応あり")
        if not pygame.mixer.music.get_busy():# Check if there is a music playing currently
            print(num)
            num = random.randint(1, 7)
            print(num)
            pygame.mixer.init()
            print(file_name)
            file_name = "./" + str(num) + ".wav"
            pygame.mixer.music.load(file_name)
            print(file_name)
            pygame.mixer.music.play()  # Play the sound
            while pygame.mixer.music.get_busy():  # Wait for the sound to finish playing
                time.sleep(1)
            time.sleep(2)  # Sleep for 3 seconds

    else:
        print("反応なし")
        time.sleep(1)  # This sleep is to wait between checks of the GPIO pin
