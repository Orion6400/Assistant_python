import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes as pj

listener= sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


talk("Hello! i am Alisa , how may i help you")


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')

            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alisha' in command:
                command = command.replace('alisha', '')
                print(command)
    except:
        pass
    return command


def run_verma():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'what is' in command:
        item = command.replace('what is', '')
        info = wikipedia.summary(item, 2)
        print(info)
        talk(info)
    elif 'who is' in command:
        item = command.replace('who is', '')
        info = wikipedia.summary(item, 2)
        print(info)
        talk(info)
    elif 'who are you' in command:
        talk("Virtual assistant created by xyz in 2021 by using python 3.9.1 on pycharm 2020.2 Plateform...")
        talk("I am able to tell the current time,simple jokes,famous personalities,places and play vedios on youtube")
        talk("thankyou")
    elif 'joke' in command:
        talk(pj.get_joke())
    elif 'sorry' in command:
        talk("you are really so dumb.....")
    else:
        talk("what next ! waiting ... otherwise showing error....")
        # talk("sorry!! can you say again...")


while True:
    run_verma()
