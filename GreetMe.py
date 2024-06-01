import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    
    

    if 0 <= hour < 12:
        speak("Good Morning, sir")
    elif 12 <= hour < 17:
        speak("Good Afternoon, sir")
    elif 17 <= hour < 21:
        speak("Good Evening, sir")
    else:
        speak("Good Night, sir")


    speak("This is friday at your service, Please tell me,how can I help you ?")
