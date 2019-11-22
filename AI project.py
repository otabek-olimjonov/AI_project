import pyttsx3
import webbrowser
import random
import speech_recognition as sr
import pyaudio
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init()

client = wolframalpha.Client('JW6Y7Q-GKWVR76AJG')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Jarvis: ' + audio)
    engine.say(audio)
    engine.runAndWait()
    

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning, Sir!')

    if currentH >=12 and currentH < 18:
        speak('Good Afternoon, Sir!')

    if currentH >=18 and currentH !=0:
        speak('Good Evening!, Sir')

greetMe()
speak('I am your Jarvis!')
speak('How may I help you?')

def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='eng')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry Sir! I did\'t get that! Try type the command')
        print(str(input('command: ')))

    return query

if __name__== '__main__':

    while True:

        query = myCommand();
        query = query.lower()

        if 'open youtube' in query:
            speak('okey')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okey')
            webbrowser.open('www.google.com')

        elif 'open email' in query:
            speak('okey')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full energy']
            speak(random.choice(stMsgs))

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'hello' in query:
            speak('Hello Sir')


        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'play music' in query:
            music_folder = 'www.youtube.com'
            music = ['/watch?v=Qz7O1WNfzSI', '/watch?v=ZE-5pgaHpwQ', '/watch?v=cDb9Vkkpx0E', '/watch?v=oXZ5j3k82HY']
            random_music = music_folder + random.choice(music)
            webbrowser.open(random_music)

            speak('Okay, here is your music! Enjoy!')

        else:
            query = query
            speak('Serching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak(results)

            except:
                 webbrowser.open('www.google.com')
        speak("If you want to continue, click Enter")
        input()
speak('Next Command! Sir!')
