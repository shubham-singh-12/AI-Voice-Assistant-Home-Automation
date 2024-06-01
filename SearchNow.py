import webbrowser
import pywhatkit
import pyttsx3
import speech_recognition
import wikipedia


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said :{query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def search_on_google(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("google", "")
        query = query.replace("search on google", "")
        query = query.replace("jarvis", "")
        query = query.replace("friday", "")
        speak("This is what i found")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            print(result)
            speak(f"According to google {result}")
        except:
            speak("No speakable output available")

def search_on_youtube(query):
    if "youtube" in query:
        speak("This is what i found on youtube")
        query = query.replace("youtube search", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done sir")

def search_on_wikipedia(query):
    if "wikipedia" in query:
        speak("Searching on wikipedia")
        query = query.replace("wikipedia", "")
        query = query.replace("search on wikipedia", "")
        query = query.replace("according to wikipedia", "")
        query = query.replace("wikipedia", "")
        query = query.replace("jarvis", "")
        query = query.replace("friday", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)
