import speech_recognition
import os
import pyttsx3
import requests
from bs4 import BeautifulSoup
import datetime
import clipboard
import pyjokes
import time as tt
from datetime import timedelta
import pyautogui
import random
from pygame import mixer
import serial




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
        recognizer.energy_threshold = 270
        audio = recognizer.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"You said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query




# ALARM FUNCTION
def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")




# TEXT to SPEECH
def textToSpeech():
    text = clipboard.paste()
    print(text)
    speak(text)




# SCREENSHOT FUNCTION
def take_screenshot():
    name_img = tt.time()
    screenshot_dir = "C:\\Users\\SHUBHAM\\Desktop\\FINAL YEAR PROJECT MATERIAL\\FRIDAY\\screenshots\\"
    name_img = f"{screenshot_dir}{name_img}.png"
    img = pyautogui.screenshot(name_img)
    img.show()
    speak("Screenshot saved")
    return name_img




# Arduino Serial Communication Setup
ser = serial.Serial('COM5', 9600, timeout=1)
def send_command_to_arduino(query):
    ser.write(query.encode())




# Initialize the mixer
mixer.init()

# Function to get the next file in the folder
def get_next_file(current_file, files):
    current_index = files.index(current_file)
    next_index = (current_index + 1) % len(files)
    return files[next_index]

# Function to get the previous file in the folder
def get_previous_file(current_file, files):
    current_index = files.index(current_file)
    previous_index = (current_index - 1) % len(files)
    return files[previous_index]

# Prompt the user for the folder path
folder_path = "C:\\Users\\SHUBHAM\\Desktop\\FINAL YEAR PROJECT MATERIAL\\FRIDAY\\music_folder"

# Get a list of all music files in the folder
music_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.mp3', '.wav', '.ogg'))]

# If there are no music files, exit
if not music_files:
    print("No music files found in the specified folder.")
    exit()

# Start with a random song
current_song = random.choice(music_files)
mixer.music.load(current_song)

music_playing = False







#MAIN FUNCTION
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

# GREET ME
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                print(query)

# THE MAIN PROGRAM IS RUNNING, BUT NOT ACCEPT THE COMMAND GIVEN BY USERS
                if "sleep" in query:
                    speak("Ok sir, you can call me anytime")
                    break




# NORMAL CONVERSATION
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great")
                elif "how r u" in query:
                    speak("i am perfectly alright")
                elif "your name" in query:
                    speak("I am friday, an ai assistant, ")
                elif "tell me your purpose" in query:
                    print("The main aim to create me is that, i am an A.I voice assistant for normal use like control Home Appliances, and do some normal tasks also like open app's, files, play music, control youtube, search on wikipedia, google, youtube also.\n"
                          "As I am a basic version of the main version that is installed at home.")
                    speak("The main aim to create me is that, i am an A.I voice assistant for normal use like control Home Appliances, and do some normal tasks also like open app's, files, play music, control youtube, search on wikipedia, google, youtube also.\n"
                          "As I am a basic version of the main version that is installed at home.")
                elif "tell something about your creator" in query:
                    print("My creater name is Mr. Shubham Singh, he is the student of MIET college, and currently he is in B.Tech CSE, fourth year. If ou want to contact him, i can give you the contact number.")
                    speak("My creater name is Mr. Shubham Singh, he is the student of MIET college, and currently he is in B.Tech CSE, fourth year. If ou want to contact him, i can give you the contact number.")
                elif "give me the contact number of your creator" in query:
                    print("+91 7037528081")
                    speak("Here, is the contact number you cn contact him.")
                elif "give me the contact detail of your creater" in query:
                    print("E-mail: shubham.singh.cse.2020@miet.ac.in \n Phone number: +91 7037528081")
                    speak("Here is the contact e-mail and phone number ID of my creater Mr. Shubham Singh")




# ARDUINO CONTROL HOME AUTOMATION

                # Send '1' to Arduino to turn on the LED
                elif "turn on led" in query:
                    send_command_to_arduino('1')
                    print("LED Turn ON")
                    speak("LED Turn ON")

                # Send '0' to Arduino to turn off the LED
                elif "turn off led" in query:
                    send_command_to_arduino('2')
                    print("LED Turn OFF")
                    speak("LED Turn OFF")

                # Send '1' to Arduino to turn ON the IGNITION
                elif "turn on ignition" in query:
                    send_command_to_arduino('3')
                    print("IGNITION Turn ON")
                    speak("IGNITION Turn ON")

                # Send '0' to Arduino to turn off the IGNITION
                elif "turn off ignition" in query:
                    send_command_to_arduino('4')
                    print("IGNITION Turn OFF")
                    speak("IGNITION Turn OFF")

                # Send 'M' to Arduino to start the fan
                elif "turn on fan" in query:
                    send_command_to_arduino('5')
                    print("FAN Turn ON")
                    speak("FAN Turn ON")

                # Send 'm' to Arduino to stop the fan
                elif "turn off fan" in query:
                    send_command_to_arduino('6')
                    print("FAN Turn OFF")
                    speak("FAN Turn OFF")

                # CONTROL FAN SPEED
                elif "fan speed " in query:
                    speed = int(query.split()[-1])
                    if 0 <= speed <= 255:
                        send_command_to_arduino("7" + str(speed))
                    else:
                        print("Invalid fan speed. Please specify a value between 0 and 255.")
                        speak("Invalid fan speed. Please specify a value between 0 and 255.")


# VLC MUSIC CONTROLLING
                elif "stop music" in query:
                    pyautogui.press("space")
                    speak("music stopped")

                elif "mute music" in query:
                    pyautogui.press("m")
                    speak("music muted")

                elif "unmute music" in query:
                    pyautogui.press("m")
                    speak("music unmuted")

                elif "next music" in query:
                    pyautogui.press("N")
                    speak("next music played")

                elif "previous music" in query:
                    pyautogui.press("P")
                    speak("previous music played")




#PLAY MUSIC FROM LOCAL SYSTEM
                elif query == "play music":
                    if music_playing:
                        print("Music is already playing.")
                    else:
                        mixer.music.play()
                        print("Playing music.")
                        music_playing = True

                elif query == "pause":
                    if music_playing:
                        mixer.music.pause()
                        print("Music paused.")
                    else:
                        print("No music is playing.")

                elif query == "next":
                    if music_playing:
                        current_song = get_next_file(current_song, music_files)
                        mixer.music.load(current_song)
                        mixer.music.play()
                        print(f"Playing next song: {current_song}")
                    else:
                        print("No music is playing.")

                elif query == "previous":
                    if music_playing:
                        current_song = get_previous_file(current_song, music_files)
                        mixer.music.load(current_song)
                        mixer.music.play()
                        print(f"Playing previous song: {current_song}")
                    else:
                        print("No music is playing.")

                elif query == "exit music":
                    mixer.music.stop()
                    print("Music stopped.")
                    mixer.quit()




# OPEN & CLOSE APP
                elif "open" in query:
                    from DictApp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from DictApp import closeappweb
                    closeappweb(query)




# SEARCH ON GOOGLE, YOUTUBE, WIKIPEDIA
                elif "youtube" in query:
                    from SearchNow import search_on_youtube
                    search_on_youtube(query)

                elif "google" in query:
                    from SearchNow import search_on_google
                    search_on_google(query)

                elif "wikipedia" in query:
                    from SearchNow import search_on_wikipedia
                    search_on_wikipedia(query)




# LATEST NEWS UPDATES
                elif "news" in query:
                    from NewsReady import latestnews
                    latestnews()




# CALCULATOR
                elif "calculate" in query:
                    from Calculate_Number import Wolframalpha
                    from Calculate_Number import calc
                    query = query.replace("calculate", "")
                    query = query.replace("friday", "")
                    calc(query)




# SEND MESSAGE ON WHATSAPP
                elif "whatsapp" in query:
                    from WhatsApp import sendMessage
                    sendMessage()




# CONTROL YOUTUBE
                elif "pause video" in query:
                    pyautogui.press("k")
                    speak("Video Paused")
                elif "play video" in query:
                    pyautogui.press("k")
                    speak("Video Played")
                elif "mute video" in query:
                    pyautogui.press("m")
                    speak("Video Muted")
                elif "unmute video" in query:
                    pyautogui.press("m")
                    speak("Video Unmuted")




# INCREASE OR DECREASE VOLUME IN YOUTUBE
                elif "increase volume" in query:
                    from keyboard import volumeup
                    speak("Increasing volume")
                    volumeup()
                elif "decrease volume" in query:
                    from keyboard import volumedown
                    speak("Decreasing volume")
                    volumedown()




# TELL THE CURRENT TEMPERATURE
                elif "temperature" in query:
                    search = "temperature in Meerut"
                    url = f"https://www.google.com/search?q={query}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    print(f"current {search} is {temp}")
                    speak(f"current {search} is {temp}")




# TELL THE CURRENT WEATHER
                elif "weather" in query:
                    search = "weather in Meerut"
                    url = f"https://www.google.com/search?q={query}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    print(f"current {search} is {temp}")
                    speak(f"current {search} is {temp}")




# SET ALARM
                elif "set an alarm" in query:
                    print("Enter the alarm time in 12-hour format (e.g., 08:30:00 AM/PM)")
                    speak("Set the time")
                    a = input("Please Enter the time: ")
                    alarm(a)
                    print(f"Alarm is set at {a}")
                    speak(f"Alarm is set at {a}")




# TEXT to SPEECH
                elif "read" in query:
                    textToSpeech()




# JOKES
                elif "joke" in query:
                    speak(pyjokes.get_joke())




# TAKE SCREENSHOT
                elif "take screenshot" in query:
                    take_screenshot()




# TELL THE CURRENT TIME
                elif "time" in query:
                    #12-hour format
                    strTime = datetime.datetime.now().strftime("%I:%M %p")
                    print(f"the current time is {strTime}")
                    speak(f"the current time is {strTime}")




# TELL ME THE PREVIOUS DAY
                elif "previous day" in query:
                    today = datetime.datetime.now()
                    previous_day = today - timedelta(days=1)
                    print(f"Yesterday was {previous_day.strftime("%A")}")
                    speak(f"Yesterday was {previous_day.strftime("%A")}")

# TELL THE CURRENT DAY
                elif "current day" in query:
                    current_day = datetime.datetime.now().strftime("%A")
                    print(f"Today is {current_day}")
                    speak(f"Today is {current_day}")

# TELL ME THE UPCOMING DAY
                elif "tomorrow day" in query:
                    today = datetime.datetime.now()
                    tomorrow = today + timedelta(days=1)
                    print(f"Tomorrow is {tomorrow.strftime("%A")}")
                    speak(f"Tomorrow is {tomorrow.strftime("%A")}")




# TELL ME THE YESTERDAY DATE
                elif "yesterday date" in query:
                    today = datetime.datetime.now()
                    yesterday_date = today - timedelta(days=1)
                    print(f"Yesterday date was {yesterday_date.strftime("%d %B, %Y")}")
                    speak(f"Yesterday date was {yesterday_date.strftime("%d %B, %Y")}")

# TELL THE CURRENT DATE
                elif "current date" in query:
                    current_date = datetime.datetime.now().strftime("%d %B, %Y")
                    print(f"Today's date is {current_date}")
                    speak(f"Today's date is {current_date}")

# TELL US THE TOMORROW DATE
                elif "tomorrow date" in query:
                    today = datetime.datetime.now()
                    tomorrow_date = today + timedelta(days=1)
                    print(f"Tomorrow date is {tomorrow_date.strftime("%d %B, %Y")}")
                    speak(f"Tomorrow date is {tomorrow_date.strftime("%d %B, %Y")}")




# REMEMBER FUNCTION
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that" "friday", " ")
                    speak("You told me to" + rememberMessage)
                    remember = open("Remember.txt", "a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt", "r")
                    speak("You told me to" + remember.read())




# CLOSE THE MAIN FUNCTION
                elif "switch off" in query:
                    speak("ok, shutting down.")
                    exit()