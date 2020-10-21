import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[2].id)
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
  speak("hello! i am alfread how may i help you today?")

def takeCommand():
  #it takes microphone input from the user and returns string output

  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("listening..")
    r.pause_treshold = 1
    audio = r.listen(source) 
  
  try:
    print("Recognizing..")
    query = r.recognize_google(audio,language='en-in')
    print(f"user said: {query}\n")

  except Exception as e:
    print(e)

    print("say that again please..")
    return "None"
  return query


wishMe()
while True:
  query = takeCommand()
  chrome = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")

  # logic for ecuting tasks based on query
  if "wikipedia" in query.casefold():
    speak('searching wikipedia...')
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query,sentences=2)
    speak("according to wikipedia")
    print(results)
    speak(results)

  elif "youtube" in query.casefold():
    chrome.open_new("https://www.youtube.com")

  elif 'open google' in query.casefold():
    chrome.open_new("https://www.google.com")

  elif 'the time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"sir, the time is{strTime}")

  elif 'play music' in query:
    music_dir = "C://Users//Amaan//Music//New folder"
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir,songs[0]))
