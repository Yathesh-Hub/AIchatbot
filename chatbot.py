import os
import speech_recognition as sr
import pyttsx3
from google.generativeai.client import configure
from google.generativeai.generative_models import GenerativeModel
import pyaudio

# Configure Gemini API
configure(api_key="AIzaSyCTRxylDWPb5X3oGXUkIYamufMfatRVzus")
model = GenerativeModel("gemini-1.5-flash")
# Initialize speech recognition and text-to-speech
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I did not understand.")
        return ""
    except sr.RequestError:
        print("Speech recognition service error.")
        return ""

def chat():
    print("Say 'quit' to exit.")
    while True:
        user_input = listen()
        if user_input.lower() == "quit":
            speak("Goodbye!")
            break
        if user_input:
            response = model.generate_content(user_input)
            answer = response.text.strip()
            print(f"AI: {answer}")
            speak(answer)

if __name__ == "__main__":
    chat()
