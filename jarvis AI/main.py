import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("I am Jarvis Sir Please tell me how may I help you")

def takeCommand():
    """It takes microphone input from user and retruns string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language= 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query



if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        chrome_path = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com")

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open("stackoverflow.com")

        elif 'play music' in query:
            webbrowser.get('chrome').open("https://music.youtube.com/watch?"
                                          "v=4OeQhAZaQbc&list=RDCLAK5uy_nlOMew8qv8HGXb9HbshuU1OgH3aL_JMKA")

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")  
            print(strtime)  
            speak(f"Sir,the time is {strtime}")

        elif 'date' in query:
            strtime = datetime.datetime.now().strftime("%m/%d/%y") 
            print(strtime)   
            speak(f"Sir,the date is {strtime}")

        elif 'open google' in query:
            webbrowser.get('chrome').open("google.com")

        elif 'open code' in query:
            code_path = "C:\Users\HP\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(code_path)
