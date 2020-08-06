import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser,os,smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("goodmorning!")
    elif hour>=12 and hour<=18:
        speak("goodafternoon!")
    else:
        speak("goodevening!")
    speak("i am Jarvis. How may i help you")

def takecommand():
    # it takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        # r.energy_threshold=30
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    # pylint: disable=unused-variable
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("devraj.kakoty@gmail.com",'*******')
    server.sendmail("devraj.kakoty@gmail.com",to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query=takecommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia",'')
            results=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")
        elif 'open code' in query:
            codepath="C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'play music' in query:
            musicdir="C:\\Music\\songs\\fav songs"
            songs=os.listdir(musicdir)
            os.startfile(os.path.join(musicdir,songs[0]))

        elif 'email' in query:
            try:
                speak("What should I say?")
                content=takecommand()
                to="devraj.kakoty@gmail.com"
                sendEmail(to,content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send your email at the moment")

        elif 'stop' in query:
            break
