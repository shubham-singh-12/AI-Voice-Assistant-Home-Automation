import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


dictapp = {"commandprompt": "cmd", "paint": "MSPaint", "word": "winword", "excel": "excel", "chrome": "chrome", "vs code": "code", "powerpoint": "powerpnt", "vlc": "vlc", "pycharm": "pycharm", "This PC": "shell:MyComputerFolder"}


#TO OPEN
def openappweb(query):
    speak({query})
    if ".com" in query or ".co.in" in query or ".org" in query or ".in" in query:
        query = query.replace("open", "")
        query = query.replace("friday", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")


#FOR CLOSING
def closeappweb(query):
    speak({query})

    #CLOSE 1 TAB
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    #CLOSE 2 TAB
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    #CLOSE 3 TAB    
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    #CLOSE 4 TAB    
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    
    #CLOSE 5 TAB
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
