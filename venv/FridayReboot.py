import webbrowser
import speech_recognition as sr
import pyaudio
import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyttsx3
import threading
from pytube import YouTube

# Function to get voice input
def getVoice():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Commmand :")
        rec.adjust_for_ambient_noise(source, duration=1)
        audio = rec.listen(source)
    try:
        text = rec.recognize_google(audio)
        print("I Heard:", text)
        execute_command(text.lower())
    except sr.UnknownValueError:
        print("I did not get that")
    except sr.RequestError:
        print("Error: Request error.")

def getYTDownload(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Error Occured While Downloading the Video !")
    print("Download Completed Master SINISTER !")


# link = input("Enter the Youtube Video URL to Download : ")
# Download(link)

# Function to perform actions based on voice commands
def getLogin():
    speak("Welcome Master Sinister. Logging in.")
    driver = webdriver.Edge()
    driver.get("http://172.16.1.1:8090/")
    Wusername = driver.find_element(By.ID, "username")
    Wusername.send_keys("MCA1003923")
    Wpassword = driver.find_element(By.ID, "password")
    Wpassword.send_keys("8359834412")
    Wpassword.send_keys(Keys.ENTER)
    time.sleep(3)
    driver.quit()
    speak("Login successful. Welcome Master Sinister.")
def getWeather():
    api_key = "5200219ca467e31a1afe47fddb4d8aa5"  # Replace this with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Ranchi"  # Replace this with the desired city name or make it user-input based

    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        weather_info = f"Current Weather is {weather}. The temperature is {temp}°C. Humidity is {humidity}%. Wind speed is {wind_speed} m/s."
        Friday(weather_info)
    else:
        Friday("Sorry, I couldn't fetch the weather information at the moment Please Try again Later")


def getERP():
    FridayVoice("Opening ERP portal.")
    driver = webdriver.Edge()
    driver.get("https://erpportal.bitmesra.ac.in/login.htm")
    driver.implicitly_wait(10)
    username = driver.find_element(By.ID, "j_username")
    username.send_keys("hellolucifer007@gmail.com")
    password = driver.find_element(By.NAME, "j_password")
    password.send_keys("123456")
    password.send_keys(Keys.ENTER)
    # time.sleep(13)
    # advanceBtn = driver.find_element(By.ID, "advancedButton")
    # advanceBtn.click()
    # time.sleep(5)
    # acceptRisk = driver.find_element(By.ID, "exceptionDialogButton")
    # acceptRisk.click()
    FridayVoice("ERP portal accessed successfully.")
    while True:
        time.sleep(1)
    driver.close()
def getPrivateSearch():
    options = webdriver.EdgeOptions()
    options.use_chromium = True
    options.add_argument("incognito")
    driver = webdriver.Edge(options=options)
    driver.get("https://duckduckgo.com/")
    while True:
        time.sleep(1)
    driver.quit()
def shutdown():
    os.system("shutdown /p")



def execute_command(command):
    if "notepad" in command:
        os.system("notepad.exe")
    elif "calculator" in command:
        os.system("calc.exe")
    elif "browser" in command:
        os.system("start msedge")  # Use "msedge" to open Microsoft Edge
    elif "shutdown" in command:
        FridayVoice("Are You Sure you want to Shutdown ?")
        response = getVoice().lower()
        if response == "yes":
            os.system("shutdown /p")
        else:
            execute_command(getVoice().lower())
    elif "exit" in command:
        thankPrompt = "Have a Good Day , Sir"
        FridayVoice(thankPrompt)
        exit()
    elif "python" in command:
        os.system("E:\Python.lnk")
    elif "thanks" in command:
        thankPrompt = "Enjoy Your Day Sir"
        FridayVoice(thankPrompt)
        exit()
    elif "lock" in command:
        os.system(r"E:\Lock\lock.bat")
    elif "help" in command:
        help()
    elif "youtube" in command:
        rec = sr.Recognizer()
        with sr.Microphone() as source:
            Friday("What do you want to watch Sir?")
            # rec.adjust_for_ambient_noise(source, duration=1)
            audio = rec.listen(source)
        try:
            text = rec.recognize_google(audio)
            Friday(f"Searching for {text} on YouTube.")
            webbrowser.open("https://www.youtube.com/results?search_query=%s" % text)
        except sr.UnknownValueError:
            FridayVoice("I did not get that")
        except sr.RequestError:
            FridayVoice("Error: Request error.")
    elif "search" in command:
        rec = sr.Recognizer()
        with sr.Microphone() as source:
            Friday("What do you want to Search Sir?")
            rec.adjust_for_ambient_noise(source, duration=1)
            audio = rec.listen(source)
        try:
            text = rec.recognize_google(audio)
            Friday(f"Searching for {text} on Google.")
            webbrowser.open("https://www.google.com/search?q=%s" % text)
        except sr.UnknownValueError:
            FridayVoice("I did not get that")
        except sr.RequestError:
            FridayVoice("Error: Request error.")

    # Add a command to open a website based on user input
    elif "open website" in command:
        # Extract the website URL from the command
        parts = command.split("open website ")[1:]
        website_url = " ".join(parts)
        # Open the specified website in the default web browser
        webbrowser.open(website_url)
        websitePrompt = f"Opening {website_url}."
        Friday(websitePrompt)
    elif "log" in command:
        getLogin()
    elif "erp" in command:
        getERP();
    elif "private" in command:
        Friday("Private Search Executed ! , What you want to Search")
        getPrivateSearch()
    elif "download video" in command:
        Friday("URL Please ! :")
        link =input("Enter URL : ")
        FridayVoice("Downloading The Video")
        getYTDownload(link)




# Function for voice assistant to speak
def FridayVoice(greet):
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 140)
        engine.setProperty("volume", 0.040)
        engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')
        engine.say(greet)
        engine.runAndWait()
    except Exception as e:
        print("Unknown Error Occurred!")

def Friday(greet):
    try:
        engine=pyttsx3.init()
        engine.setProperty("rate",180)
        engine.setProperty("pitch",0.40)
        engine.setProperty("volume",0.040)
        engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')
        engine.say(greet)
        engine.runAndWait()
    except Exception as e:
        print("Unknown Error Occurred!")
# Sample functions (getLogin, getERP, help, etc.) should be defined based on the specific functionalities you want to implement.
# For instance, getLogin may contain code to perform login operations.

# Entry point: voice assistant
print("Friday Mark I [BETA]")
FridayVoice("Welcome Sir!")
FridayVoice("Where You want to Start First !")
# Start voice recognition
mic=sr.Microphone(device_index=1)
while True:
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Command:")
        rec.adjust_for_ambient_noise(source, duration=1)
        # time.sleep(0.5)
        audio = rec.listen(source)
    try:
        text = rec.recognize_google(audio)
        print("I Heard:", text)
        execute_command(text.lower())
    except sr.UnknownValueError:
        print("I did not get that")
    except sr.RequestError as e:
        print("Error:", e)
