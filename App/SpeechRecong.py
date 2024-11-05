import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
voice = pyttsx3.init()


def speakNow(command):
    voice.say(command)
    voice.runAndWait()

# Speech recognition from microphone
with sr.Microphone() as source:
    print("Adjusting for ambient noise...")
    recognizer.adjust_for_ambient_noise(source, duration=2)
    print("Speak now...")
    audio = recognizer.listen(source)

# Recognize and print
try:
    text = recognizer.recognize_google(audio)
    print("Did you say:", text.lower())
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError:
    print("Could not request results")

speakNow(text)