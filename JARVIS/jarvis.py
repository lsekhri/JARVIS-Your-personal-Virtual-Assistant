
import pyttsx3
import speech_recognition as sr  # module will help us understand user from microphone
import datetime  # datetime would help determine the current
import wikipedia
import webbrowser
import os


engine=pyttsx3.init('nsss') #nsss used in mac
voices=engine.getProperty('voices')
print(voices[5].id)
engine.setProperty('voice',voices[0].id)

#the speak function  would recieve the audio and make the engine say the words 
def speak(audio):
     engine.say(audio)
     engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
         speak("Good Morning user")
    elif hour>=12 and hour<17:
         speak("Good afternoon user")
    elif hour>=17 and hour<21:
         speak("Good evening user")
    else:
         speak("it's night time you should be slepping by now user")
    speak("Hello Iron Man, I am Jarvis your personal assistant, how may I help you")

def takeCommand():
     r=sr.Recognizer() #helps in recogomizing the audio
     with sr.Microphone() as source:   #Will help in catching error
         print("I am listening right now")
         r.pause_threshold=1 #while speaking the user can stop for a little time and it would still listen
         audio=r.listen(source)
     try:
             print("I am Recogonizing right now")
             query=r.recognize_google(audio,language='en-in')
             print(f"The User said: {query}\n")
     except Exception as e:
             print(e)

             print("Sorry I didn't understand, can you say that again please")
             return "None"
     return query


if __name__ == "__main__":
     wish()
     ag=True
     while ag:
         query=takeCommand().lower()
         if 'wikipedia' in query:
             speak("I am searching in wikipedia right now")
             query=query.replace("wikipedia","") 
             results=wikipedia.summary(query,sentences=2) #summary being a method in the wikipedia module
             speak("According to Wikipedia")
             print(results)
             speak(results) 
         elif 'youtube'in query:
             webbrowser.open("http://www.youtube.com")
         elif 'google' in query:
             webbrowser.open("https://www.google.com")
         elif 'stackoverflow' in query:
             webbrowser.open("https://stackoverflow.com")
         elif 'the time' in query:
             strTime=datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Sir,the time right now is {strTime}")
         elif 'code' in query:
             codep="/Users/lakshsekhri/Downloads/VisualStudioCode-2.app"
             os.system("open "+codep)
         
         
         elif 'stop' in query:
              ag=False
             



          




  
