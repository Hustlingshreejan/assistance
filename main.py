import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime


#sapi5 to take a voice given by windows api to use inbuilt voice(computer's voice)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
#voices [0] means male's voice and 1 means female's voice
engine.setProperty('voice', voices[0].id)


def speak(audio):
    '''This function will speak the sentence given in the argument'''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    # print(hour)
    if hour >=0 and hour <12:
        speak(f"Good Morning! it's {hour} {minute} AM")
    elif hour >=12 and hour<5:
        speak(f"Good Afternoon! it's {hour} {minute} PM")
    else:
        speak(f"Good Evening! it's {hour}, {minute} PM")

    speak("Namas tey! I am Rajesh Hamal. Please tell me how may i help you.")

def takeCommand():
    ''' It takes micro phone input from the user and returns string output to show in command '''

    #Recognizer class will help to recognize the audio we speak
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        #This threshold will wait for 1 second. If there is gap of 1 second, it will
        #take it as sentence complited
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Please say that again...")
        return "None"
    return query

if __name__ == '__main__':
    # wishMe()
    while True:
        query = takeCommand().lower()
    #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

