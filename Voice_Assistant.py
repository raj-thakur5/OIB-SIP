import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import pywhatkit as kit

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# take command from user
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query

# greet user
def greet_user():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am JARVIS, how may I assist you?")

# search on wikipedia
def search_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    speak(results)

# Open YouTube
def open_youtube(url):
    url = 'https://www.youtube.com/'
    webbrowser.open(url)

# Open Google
def open_google(url):
    url = 'https://www.google.com/search?q='
    webbrowser.open(url)

# send an email
def send_email(to, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nirajdas6664521@gmail.com', '*')
    msg = 'Subject: {}\n\n{}'.format(subject, message)
    server.sendmail('nirajdas6664521@gmail.com', to, msg)
    server.quit()

# play a song on YouTube
def play_song(song):
    kit.playonyt(song)

# Main function
def main():
    greet_user()
    while True:
        query = take_command().lower()

        # Search on Wikipedia
        if 'wikipedia' in query:
            query = query.replace('wikipedia', '')
            search_wikipedia(query)
            break

        # Search on Google
        elif 'google' in query:
            query = query.replace('google', '')
            open_google(url='https://www.google.com/search?q=')
            break

        # Send an email
        elif 'send email' in query:
            speak("To whom should I send the email?")
            to = take_command().lower()
            speak("What should be the subject of the email?")
            subject = take_command().lower()
            speak("What should be the message of the email?")
            message = take_command().lower()
            send_email(to, subject, message)
            break

        # Play a song on YouTube
        elif 'play' in query:
            query = query.replace('play', '')
            play_song(query)
            break

        # Opening YouTube stream
        elif 'open youtube' in query:
            query = query.replace('open youtube', '')
            open_youtube(url="https://www.youtube.com/")
            break

        # Exit chatbot
        elif 'shutdown' in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()