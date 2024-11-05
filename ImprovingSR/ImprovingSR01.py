import speech_recognition as sr
import pyttsx3
import time

# Initialize recognizer and voice engine
recognizer = sr.Recognizer()
voice = pyttsx3.init()

def speak_now(command):
    """Speaks the command using text-to-speech."""
    voice.say(command)
    voice.runAndWait()

def set_voice_properties():
    """Sets voice properties such as rate and volume."""
    rate = voice.getProperty('rate')
    voice.setProperty('rate', rate - 10)  # Decrease the speaking rate for clarity
    volume = voice.getProperty('volume')
    voice.setProperty('volume', volume + 0.1)  # Increase volume
    # You can set voice type if needed by checking available voices
    voices = voice.getProperty('voices')
    voice.setProperty('voice', voices[0].id)  # Change to another voice (0 for male, 1 for female)

def recognize_speech():
    """Recognizes speech and returns the recognized text."""
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Speak now...")

        while True:
            try:
                audio = recognizer.listen(source, timeout=5)  # Timeout for user input
                text = recognizer.recognize_google(audio)
                return text.lower()

            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio. Please try again.")
                speak_now("I could not understand the audio. Please try again.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                speak_now("There seems to be an issue with the speech recognition service. Please check your connection.")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                speak_now("An unexpected error occurred. Please try again.")
                break

def execute_command(command):
    """Executes a command based on recognized speech."""
    if "hello" in command:
        response = "Hello! How can I assist you today?"
        print(response)
        speak_now(response)
    elif "time" in command:
        current_time = time.strftime("%H:%M:%S")
        response = f"The current time is {current_time}."
        print(response)
        speak_now(response)
    elif "stop" in command:
        response = "Stopping the program. Goodbye!"
        print(response)
        speak_now(response)
        return True  # Return True to stop the loop
    else:
        response = "I did not recognize that command."
        print(response)
        speak_now(response)
    return False  # Return False to continue listening

# Set voice properties
set_voice_properties()

# Main loop
running = True
while running:
    recognized_text = recognize_speech()
    print("Did you say:", recognized_text)

    if recognized_text:
        running = execute_command(recognized_text)
