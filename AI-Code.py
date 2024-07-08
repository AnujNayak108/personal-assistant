#AI Which Repeats What You Said 

import pyttsx3
import speech_recognition as sr
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == "__main__":
    speak("hello anuj")





def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something")
        r.pause_threshold = 1
        audio = r.listen(source)
        
            
        


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: , {query}\n")

    except Exception as e:
        #print(e)

        print("say that again please")
        return "none"
    return query

if __name__ == "__main__":

    while True:
        
        query = takeCommand().lower()

        if '' in query:
            speak(query)
       
