import pyttsx3
import datetime
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


extractedtime = open("Alarmtext.txt", "rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt", "r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis", "")
    timenow = timenow.replace("set an alarm", "")
    timenow = timenow.replace(" and ", ":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        # %H = Hours, %M = Minutes, %S = Seconds, %p = AM/PM
        currenttime = datetime.datetime.now().strftime("%I:%M:%S %p")
        if currenttime == Alarmtime:
            speak("Alarm ringing")
            #We can choose any music or ringtone 
            os.startfile("Moye More.mp3") 
        elif currenttime + "00:00:30" == Alarmtime:
            exit()


ring(time)
