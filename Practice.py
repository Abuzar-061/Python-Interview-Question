import winsound
import pyttsx3
import keyboard

speak = pyttsx3.init()

speak.say("Bomb Has been Planted Abuzar Run !")
speak.runAndWait()
print("Press ESC to exit")
while True:
    winsound.Beep(1000,500)
    if keyboard.is_pressed('esc'):
        break