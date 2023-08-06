import os
import sys
import webbrowser

import requests
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import smtplib
from bs4 import BeautifulSoup
import pyautogui


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command

def temp():
    search = "temperature in Gujarat"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div",class_ = "BNeawe").text
    print(f"The temperature outside is {temperature}")
    talk(f"The temperature outside is {temperature}")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vedantvagnihotri@gmail.com', 'Vedant@7110')
    server.sendmail('vedantvagnihotri@gmail.com', to, content)
    server.close()

def myLocation():
    current_map = "https://www.google.com/maps/place/Nirnay+Nagar,+Ahmedabad,+Gujarat+380081/@23.0734237,72.5604735,21z/data=!4m5!3m4!1s0x395e83675e8be929:0x275bea7bd2d36b70!8m2!3d23.0698718!4d72.5510887"
    webbrowser.open(current_map)
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_q = requests.get(url)
    geo_d = geo_q.json()
    state = geo_d['city']
    country = geo_d['country']
    print(f"You are in {state, country}")
    talk(f"You are in {state, country}")




def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'wikipedia' in command:
        print("Searching Wikipedia...")
        talk("Searching Wikipedia...")
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'hello' in command:
        print("Hello sir, what can I do for you?")
        talk("Hello sir, what can I do for you?")
    elif 'thank' in command:
        print("No problem sir!")
        talk("No Problem sir!")
    elif 'exit' in command:
        print("Ok sir!")
        talk("Ok sir!")
        sys.exit()
    elif 'roblox' in command:
        print("Opening Roblox!")
        talk("Opening Roblox!")
        webbrowser.open("https://www.roblox.com/home")
    elif 'google' in command:
        print("Opening Google Chrome!")
        talk("Opening google chrome!")
        webbrowser.open("https://www.google.com/")
    elif 'youtube' in command:
        print("Opening YouTube!")
        talk("Opening YouTube!")
        webbrowser.open("https://www.youtube.com/")
    elif 'team' in command:
        print("Opening Microsoft Teams...")
        talk("Opening Microsoft Teams...")
        teams = ("C:\\Users\\vedant agnihotri\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe")
        os.startfile(teams)
    elif 'vs code' in command:
        print("Opening Visual Studio...")
        talk("Opening Visual Studio...")
        vsCode = ("D:\\Vedant's stuff\\Microsoft VS Code\\Code.exe")
        os.startfile(vsCode)
    elif 'email' in command:
        try:
            talk("What should I send?")
            content = take_command()
            print(content)
            talk("Enter a Email Address to send the message...")
            to = input(str("Enter a Email Address: "))
            print("Sending Email...")
            talk("Please wait sir, the email is being sent...")
            sendEmail(to, content)
            print("Email has been sent!")
            talk("Email has been sent!")
        except Exception as e:
            print(e)
            talk("Sorry sir, I am not able to send the email")
    elif 'temperature' in command:
        temp()
    elif 'volume up' in command:
        pyautogui.press("volumeup")
    elif 'volume down' in command:
        pyautogui.press("volumedown")
    elif 'mute' in command or 'volume mute' in command:
        pyautogui.press("volumemute")
    elif 'my location' in command:
        myLocation()
    elif 'who are you' or 'what are you' in command:
        print('I am an AI programmed by Vedant Agnihotri. I am named Jarvis. Sir?')    
        talk('I am an AI programmed by Vedant Agnihotri. I am named Jarvis. Sir?')
    elif 'instagram' or 'insta' in command:
        webbrowser.open('https://www.instagram.com/ig_vedxnt/')
        print('Opening Instagram...')
        talk('Opening Instagram...')
    else:
        print("Say that again please")
        talk("Say that again please")

while True:
    run_jarvis()