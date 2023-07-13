import RPi.GPIO as GPIO
import time
import pygame.mixer

GPIO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN)


while True:
    if GPIO.input(GPIO_PIN) == GPIO.HIGH:
        print("反応あり")
        if not pygame.mixer.music.get_busy():# Check if there is a music playing currently
            pygame.mixer.init()
            pygame.mixer.music.load('./sound.wav')
            pygame.mixer.music.play()  # Play the sound
            while pygame.mixer.music.get_busy():  # Wait for the sound to finish playing
                time.sleep(1)
            time.sleep(2)  # Sleep for 3 seconds

    else:
        print("反応なし")
        time.sleep(1)  # This sleep is to wait between checks of the GPIO pin
