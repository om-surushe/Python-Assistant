# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 20:31:53 2021

@author: Harsh
"""

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(chrome_path))

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour<=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am pepper, how can i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold=1
        audio= r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("User said: ", query)

    except Exception as e:
        print("say that againn please")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    m=0
    while True:
        query = takeCommand().lower()
        strtime= datetime.datetime.now().strftime('%H:%M:%S')
        hour = int(strtime[:2])
        minute = int(strtime[3:5])
        seconds = int(strtime[6:])
    
        print(hour)
        print(minute)
        print(seconds)
        
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=2)
            speak('Accordinng to wikipedia')
            print(results)
            speak(results)      
            
        
        elif 'the time' in query:
            strtime= datetime.datetime.now().strftime('%H:%M:%S')
            print(f' sir , the time is {strtime}')
            
            
        elif 'website open' in query:
            print("sir please tell me the url")
            url = takeCommand().lower()
            webbrowser.get("chrome").open_new_tab(url)
            
        elif hour == 13 and m==0:
            m=m+1
            webbrowser.get("chrome").open_new_tab('https://meet.google.com/xow-pdxg-jvy')
            
        elif 'python' in query:
            webbrowser.get("chrome").open_new_tab('https://meet.google.com/xow-pdxg-jvy')
