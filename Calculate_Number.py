import wolframalpha
import pyttsx3
import speech_recognition






engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Wolframalpha(query):
    api_key = "YOUR_WOLFRAMALPHA_API"
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("Value is not answerable")

def calc(query):
    Term = str(query)
    Term = Term.replace("Friday","")
    Term = Term.replace("Multiply","*")
    Term = Term.replace("Plus","+")
    Term = Term.replace("Minus","-")
    Term = Term.replace("Divide","/")

    Final = str(Term)
    try:
        result = Wolframalpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")
