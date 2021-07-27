import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pyjokes
import re
import python_weather
import asyncio




engline = pyttsx3.init('sapi5')
voices = engline.getProperty('voices')
print(voices[0].id)
engline.setProperty('voices', voices[0].id)


def speak(audio):
    engline.say(audio)
    engline.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am jarvis sir. how may I help you" )

def takeCommand():
    # It takes microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    except Exception as e:
        #print(e)
        print("Say that again please...")
    else:
        speak("sorry i could not understand  ")
    return "none"
    return query


if __name__ == "__main__":
    wishMe()
    while (1==1):
        query = takeCommand().lower()




        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'in google' in query:
            speak('Searching webbrowser...')
            query = query.replace("in google search", "")
            results = webbrowser.open(query)
            speak("According to  web search")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")
            speak("opening whatsapp")

        elif 'open pluralsight' in query:
            webbrowser.open("pluralsight.com")
            speak("opening pluralsight")

        elif 'cool math games' in query:
            webbrowser.open("coolmathgames.com")
            speak("opening cool math games")




        elif 'play music' in query:
            music_dir = 'C:\\Souradeep\\Music1'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'a joke' in query:
            speak(pyjokes.get_joke())


        elif 'info' in query:
            speak("program name is jarvis,    inventer is souradeep,  codding language is python by using pycharm")



        elif 'open calculator' in query:
            codePath = "C:\\Users\\satya\\OneDrive\\Desktop\\Calculator"
            os.startfile(codePath)
            speak("opening calculator")

        elif 'open map' in query:
            codePath = "C:\\Users\\satya\\OneDrive\\Desktop\\Maps"
            os.startfile(codePath)
            speak("opening map ")


        elif 'open camera' in query:
            codePath = "C:\\Users\\satya\\OneDrive\\Desktop\\Camera"
            os.startfile(codePath)
            speak("opening camera"
                  "")

        elif 'quit' in query:
            speak("ok, bye bye")
            quit()

        elif 'stop' in query:
            speak("ok, bye bye")
            quit()

