import time

from gpiozero import Button

button = Button(17)
while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")
    time.sleep(0.5)
