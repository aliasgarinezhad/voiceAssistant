import pyttsx3
import datetime
import speech_recognition as sr
import subprocess
import wolframalpha
import tkinter
import json
import random
import operator
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import nltk


def tts_engine_init():
    global engine
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def start():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir !")

    elif 12 <= hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")


def upload_update_file():
    speak("i started uploading process. notif you when finished")
    speak("uploading complete.")


def take_command():

    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("i am listening")
    with mic as source:
        audio = recognizer.listen(source)

    print("processing ...")

    try:
        command = recognizer.recognize_google(audio)
        print(command)
        return command
    except Exception:
        speak("i dont understand your command")
        return "None"


tts_engine_init()
start()


while True:

    # input = take_command().lower()
    command = input().lower()

    if 'wikipedia' in nltk.word_tokenize(command):
        speak('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=3)
        speak("According to Wikipedia")
        speak(results)

    elif 'open youtube' in command:
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")

    elif 'open google' in command:
        speak("Here you go to Google\n")
        webbrowser.open("google.com")

    elif 'open stackoverflow' in command:
        speak("Here you go to Stack Over flow.Happy coding")
        webbrowser.open("stackoverflow.com")

    elif 'play music' in command or "play song" in command:
        speak("Here you go with music")
        # music_dir = "G:\\Song"
        music_dir = "C:\\Users\\GAURAV\\Music"
        songs = os.listdir(music_dir)
        print(songs)
        random = os.startfile(os.path.join(music_dir, songs[1]))

    elif 'the time' in command:
        strTime = datetime.datetime.now().strftime("% H:% M:% S")
        speak(f"Sir, the time is {strTime}")

    elif 'open opera' in command:
        codePath = r"C:\\Users\\GAURAV\\AppData\\Local\\Programs\\Opera\\launcher.exe"
        os.startfile(codePath)

    elif 'email to gaurav' in command:
        try:
            speak("What should I say?")
            content = take_command()
            to = "Receiver email address"
            #sendEmail(to, content)
            speak("Email has been sent !")
        except Exception as e:
            print(e)
            speak("I am not able to send this email")

    elif 'send a mail' in command:
        try:
            speak("What should I say?")
            content = take_command()
            speak("whome should i send")
            to = command()
            #sendEmail(to, content)
            speak("Email has been sent !")
        except Exception as e:
            print(e)
            speak("I am not able to send this email")

    elif 'how are you' in command:
        speak("I am fine, Thank you")
        speak("How are you, Sir")

    elif 'fine' in command or "good" in command:
        speak("It's good to know that your fine")

    elif "change my name to" in command:
        command = command.replace("change my name to", "")
        assname = command

    elif "change name" in command:
        speak("What would you like to call me, Sir ")
        assname = take_command()
        speak("Thanks for naming me")

    elif "what's your name" in command or "What is your name" in command:
        speak("My friends call me")
        speak(assname)
        print("My friends call me", assname)

    elif 'exit' in command:
        speak("Thanks for giving me your time")
        exit()

    elif "who made you" in command or "who created you" in command:
        speak("I have been created by Gaurav.")

    elif 'joke' in command:
        speak(pyjokes.get_joke())

    elif "calculate" in command:

        app_id = "Wolframalpha api id"
        client = wolframalpha.Client(app_id)
        indx = command.lower().split().index('calculate')
        command = command.split()[indx + 1:]
        res = client.query(' '.join(command))
        answer = next(res.results).text
        print("The answer is " + answer)
        speak("The answer is " + answer)

    elif 'search' in command or 'play' in command:

        command = command.replace("search", "")
        command = command.replace("play", "")
        webbrowser.open(command)

    elif "who i am" in command:
        speak("If you talk then definitely your human.")

    elif "why you came to world" in command:
        speak("Thanks to Gaurav. further It's a secret")

    elif 'power point presentation' in command:
        speak("opening Power Point presentation")
        power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
        os.startfile(power)

    elif 'is love' in command:
        speak("It is 7th sense that destroy all other senses")

    elif "who are you" in command:
        speak("I am your virtual assistant created by Gaurav")

    elif 'reason for you' in command:
        speak("I was created as a Minor project by Mister Gaurav ")

    elif 'change background' in command:
        ctypes.windll.user32.SystemParametersInfoW(20,
                                                   0,
                                                   "Location of wallpaper",
                                                   0)
        speak("Background changed successfully")

    elif 'open bluestack' in command:
        appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
        os.startfile(appli)

    elif 'news' in command:

        try:
            jsonObj = urlopen(
                '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
            data = json.load(jsonObj)
            i = 1

            speak('here are some top news from the times of india')
            print('''=============== TIMES OF INDIA ============''' + '\n')

            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                speak(str(i) + '. ' + item['title'] + '\n')
                i += 1
        except Exception as e:

            print(str(e))


    elif 'lock window' in command:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()

    elif 'shutdown system' in command:
        speak("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')

    elif 'empty recycle bin' in command:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("Recycle Bin Recycled")

    elif "don't listen" in command or "stop listening" in command:
        speak("for how much time you want to stop jarvis from listening commands")
        a = int(take_command())
        time.sleep(a)
        print(a)

    elif "where is" in command:
        command = command.replace("where is", "")
        location = command
        speak("User asked to Locate")
        speak(location)
        webbrowser.open("https://www.google.nl / maps / place/" + location + "")

    elif "camera" in command or "take a photo" in command:
        ec.capture(0, "Jarvis Camera ", "img.jpg")

    elif "restart" in command:
        subprocess.call(["shutdown", "/r"])

    elif "hibernate" in command or "sleep" in command:
        speak("Hibernating")
        subprocess.call("shutdown / h")

    elif "log off" in command or "sign out" in command:
        speak("Make sure all the application are closed before sign-out")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])

    elif "write a note" in command:
        speak("What should i write, sir")
        note = take_command()
        file = open('jarvis.txt', 'w')
        speak("Sir, Should i include date and time")
        snfm = take_command()
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)

    elif "show note" in command:
        speak("Showing Notes")
        file = open("jarvis.txt", "r")
        print(file.read())
        speak(file.read(6))

    elif "update assistant" in command:
        speak("After downloading file please replace this file with the downloaded one")
        url = '# url after uploading file'
        r = requests.get(url, stream=True)

        with open("Voice.py", "wb") as Pypdf:

            total_length = int(r.headers.get('content-length'))

            for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                   expected_size=(total_length / 1024) + 1):
                if ch:
                    Pypdf.write(ch)

    # NPPR9-FWDCX-D2C8J-H872K-2YT43
    elif "mohsen" in command:
        speak("yes, sir")

    elif "weather" in command:

        # Google Open weather website
        # to get API of Open weather
        api_key = "Api key"
        base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
        speak(" City name ")
        print("City name : ")
        city_name = take_command()
        complete_url = base_url + "appid =" + api_key + "&q =" + city_name
        response = requests.get(complete_url)
        x = response.json()

        if x["code"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            print(" Temperature (in kelvin unit) = " + str(
                current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                current_pressure) + "\n humidity (in percentage) = " + str(
                current_humidiy) + "\n description = " + str(weather_description))

        else:
            speak(" City Not Found ")

    elif "send message " in command:
        # You need to create an account on Twilio to use this service
        account_sid = 'Account Sid key'
        auth_token = 'Auth token'
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=take_command(),
            from_='Sender No',
            to='Receiver No'
        )

        print(message.sid)

    elif "wikipedia" in command:
        webbrowser.open("wikipedia.com")

    elif "Good Morning" in command:
        speak("A warm" + command)
        speak("How are you Mister")
        speak(assname)

    # most asked question from google Assistant
    elif "will you be my gf" in command or "will you be my bf" in command:
        speak("I'm not sure about, may be you should give me some time")

    elif "how are you" in command:
        speak("I'm fine, glad you me that")

    elif "i love you" in command:
        speak("It's hard to understand")

    elif "what is" in command or "who is" in command:

        # Use the same API key
        # that we have generated earlier
        client = wolframalpha.Client("API_ID")
        res = client.query(command)

        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except StopIteration:
            print("No results")

# elif "" in query:
# Command go here
# For adding more commands
