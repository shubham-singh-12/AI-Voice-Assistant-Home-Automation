import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime





engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        recognizer.pause_threshold = 0.5
        recognizer.energy_threshold = 300
        audio = recognizer.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"You said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))

update = int((datetime.now()+timedelta(minutes=2)).strftime("%M"))

def sendMessage():
    speak("Whom do you want to message")
    a = int(input('''Person 1 - Press 1,
    Person 2 - Press 2'''))
    if a == 1:
        speak("What's the message")
        message = str(input("Enter the Message: "))
        pywhatkit.sendwhatmsg("+91 6239312987", message, time_hour=strTime, time_min=update)

    elif a == 2:
        speak("What's the message")
        message = str(input("Enter the Message: "))
        pywhatkit.sendwhatmsg("+91 6239312987", message, time_hour=strTime, time_min=update)