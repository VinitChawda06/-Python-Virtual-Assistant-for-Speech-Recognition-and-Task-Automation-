import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Define function for virtual assistant to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Define function to take command from microphone
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5)

        except:
            speak("I didn't hear anything. Goodbye!")
            exit()

    try:
        print("Recognizing...")
        speak("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Please say that again...")
        speak("Please say that again...")
        return "None"

    return query

# Define function for virtual assistant to wish user based on time of day
def wish_me():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("How may I assist you?")

if __name__ == '__main__':
    wish_me()

    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'play music' in query:
            music_dir = 'C:\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'quit' in query:
            speak("Goodbye!")
            exit()

