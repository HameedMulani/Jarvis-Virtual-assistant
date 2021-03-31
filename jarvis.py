import pyttsx3 #pip inslall pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >=12 and hour < 17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("I am Jarvis Sir, Please tell me how can i help you?!")

def takeCommand():
 # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening...")
       r.pause_threshold = 1
       audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    # speak("jarvis is good")
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()

        #logic to exicute task based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia -> ")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.co.in/")

        elif 'open stack overflow' in query:
            webbrowser.open("https://www.stackoverflow.com/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the Time is {strTime}\n")