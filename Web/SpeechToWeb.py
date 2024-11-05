import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

if __name__ == "__main__":
    # Set the URL prefix for easier search interpretation
    url_prefix = "https://www.google.com/search?q="

    # Use the Microphone class to access the microphone
    with sr.Microphone() as source:
        # Adjust for ambient noise to improve recognition accuracy
        recognizer.adjust_for_ambient_noise(source, duration=3)

        print("Please say something to open...")

        # Listen to the user's input
        audio = recognizer.listen(source)
        print("Hearing...")

        try:
            # Use Google's speech recognition to convert audio to text
            destination = recognizer.recognize_google(audio)
            print("You asked me to open: " + destination)

            # Add the search URL prefix to the recognized text
            search_url = url_prefix + destination

            # Open the constructed URL in the default web browser
            webbrowser.open(search_url)

        except Exception as e:
            # Handle any errors during recognition or URL opening
            print("Error:", str(e))
