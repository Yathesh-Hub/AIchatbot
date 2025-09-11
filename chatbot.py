import tkinter as tk
from tkinter import scrolledtext
import threading
import speech_recognition as sr
import pyttsx3
from speech_recognition.recognizers.whisper_local.whisper import recognize

engine = pyttsx3.init()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        chat_display.insert(tk.END,"Listening..\n")
        chat_display.see(tk.END)
        try:
            audio=recognizer.listen(source,timeout=5)
            text=recognizer.recognize_google(audio)
            chat_display.insert(tk.END,f"You:{text}\n","user")
            chat_display,see(tk.END)
            respond(text)
            