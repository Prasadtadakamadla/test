import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Prasad!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Prasad!")
    else:
        speak("Good Evening Prasad!")
    speak("I am Jarvis. How can I assist you today?")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {query}")
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            query = None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            query = None
    return query

def jarvis():
    wish_me()
    while True:
        query = listen().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Prasad, the time is {str_time}")
        elif 'exit' in query or 'stop' in query:
            speak("Goodbye Prasad!")
            break
        else:
            speak("I am not sure how to answer that. Can you try asking something else?")

if __name__ == "__main__":
    jarvis()