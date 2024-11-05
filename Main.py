import speech_recognition
import pyttsx3

sr = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source2:
    print("Silence please")

    sr.adjust_for_ambient_noise(source2, duration=2)

    print(" Speak now please...")

    audio2 = sr.listen(source2)

    text = sr.recognize_google(audio2)
    text = text.lower()

    print("Did you say:- " + text)
