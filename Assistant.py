import pywhatkit
import requests
import speedtest
import pyautogui  # SCREENSHOTS
import pyjokes
from tkinter import *
import os
import webbrowser
import operator
from PyDictionary import PyDictionary
# from playsound import playsound
from googletrans import Translator
import pyttsx3
import speech_recognition as sr
import datetime
import psutil
import main2

if main2.q == 5 and main2.e == 1:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id)

    name_assistant = "AI"

    window = Tk()

    global var
    global var1

    var = StringVar()
    var1 = StringVar()


    def Cpu_Battery():
        usage = psutil.sensors_battery()
        var.set('CPU is at ' + str(usage.percent) + ' percent')
        window.update()
        speak('CPU is at ')
        speak(str(usage.percent) + ' percent')


    def SpeedTest(query):
        speak("Checking Speed...")
        speed = speedtest.Speedtest()
        downloading = speed.download()
        correctdown = int(downloading / 800000)
        uploading = speed.upload()
        correctupload = int(uploading / 800000)
        var.set("Wait a moment Please")
        window.update()
        speak("Wait a moment Please")
        if 'uploading' in query:
            var.set(f"The Uploading Speed is {correctupload} mbps")
            window.update()
            speak(f"The Uploading Speed is {correctupload} mbps")
        elif 'downloading' in query:
            var.set(f"The Downloading Speed is {correctdown} mbps")
            window.update()
            speak(f"The Downloading Speed is {correctdown} mbps")
        else:
            var.set(f"The Downloading is {correctdown} and the uploading speed is {correctupload} mbps")
            window.update()
            speak(f"The Downloading is {correctdown} and the uploading speed is {correctupload} mbps")


    def Trans():
        speak("Tell Me The Line!")
        line = TakeHindi()
        translate = Translator()
        result = translate.translate(line)
        text = result.text
        var.set(f"The translation for this line is:" + text)
        window.update()
        speak(f"The translation for this line is:" + text)


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()


    def Music():
        var.set("Tell me the name of the song")
        window.update()
        speak("Tell me the name of the song")
        musicName = takeCommand().lower()
        speak("From your laptop or internet")
        choice = takeCommand().lower()

        print(choice, musicName)
        if 'laptop' in choice:

            if 'ringtone' in musicName:
                os.startfile('C:\\Users\\DELL\\Music\\iphone-ringtone-47958.mp3')
                var.set("Your song has been started! Enjoy Mam")
                window.update()
                speak("Your song has been started! Enjoy Mam")

            if 'latest' in musicName:
                os.startfile('C:\\Users\\DELL\\Music\\classic-cell-phone-21543.mp3')
                var.set("Your song has been started! Enjoy Mam")
                window.update()
                speak("Your song has been started! Enjoy Mam")

        elif 'internet' in choice:
            pywhatkit.playonyt(musicName)
            var.set("Your song has been started! Enjoy Mam")
            window.update()
            speak("Your song has been started! Enjoy Mam")


    def news():
        var.set("Tell me news title")
        window.update()
        speak("Tell me the news title")
        newstitle = takeCommand().lower()

        pywhatkit.playonyt(newstitle)


    def screenshot():

        var.set("What is the name of the file")
        window.update()
        speak("What is the name of the file")
        paths = takeCommand().lower()
        path = "D:/Screenpix/" + paths + ".png"
        img = pyautogui.screenshot()
        img.save(path)
        var.set("Succesfully saved")
        window.update()
        speak("Succesfully saved")


    def openapps(query):
        var.set("Ok mam, just a second")
        window.update()
        speak("Ok mam, just a second")

        if 'adobe' in query:
            os.startfile("C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe")

        elif 'notepad' in query:
            os.startfile("C:\\WINDOWS\\system32\\notepad.exe")

        elif 'code' in query:
            os.startfile("C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'maps' in query:
            webbrowser.open('https://www.google.co.in/maps/@17.3905892,78.4112494,13z?hl=en')

        elif 'facebook' in query:

            webbrowser.open('https://www.facebook.com/')

        speak("Your command has been completed mam!")


    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            var.set("Good Morning!!!")
            window.update()
            speak("Good Morning!!!")

        elif hour >= 12 and hour < 18:

            var.set("Good Afternoon!!!")
            window.update()
            speak("Good Afternoon!!!")
        else:
            var.set("Good Afternoon!!!")
            window.update()
            speak("Good Afternoon!!!")

        speak("I am AI. How may i help you")


    def calci():
        try:
            var.set("Numbers please")
            window.update()
            speak("Numbers please")
            query1 = takeCommand()

            q = query1.split(" ")
            print(q)
            op1 = (q[0])
            op = q[1]
            op2 = q[2]
            evaluate(op1, op, op2)
        except:
            var.set("Wrong input unable to recognize try again")
            window.update()
            speak("Wrong input unable to recognize try again")
            Task()
            # calci()


    def evaluate(opp1, ope, opp2):
        opp1, opp2 = int(opp1), int(opp2)
        var.set(str(get_operator(ope)(opp1, opp2)))
        window.update()
        speak(str(get_operator(ope)(opp1, opp2)))


    def get_operator(op):
        try:
            return {
                '+': operator.add,
                '-': operator.sub,
                'x': operator.mul,
                'divided': operator.__truediv__,
            }[op]
        except:
            speak("Wrong input unable to recognize try again")
            Task()


    # 22H49M55S

    def TakeHindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing...")
                query = command.recognize_google(audio, language='hi')
                print(f"You Said: {query}")
            except Exception as e:
                return "None"

            return query.lower()


    def Temperature():
        api = 'http://api.openweathermap.org/data/2.5/weather?q=Hyderabad&appid=812fc55d7dac13a0fa4a1d822c650375'
        json_data = requests.get(api).json()
        print(json_data)
        data = json_data['weather'][0]['description']
        var.set(data)
        window.update()
        speak(data)
        data = json_data['main']['temp']
        data = str(round(data / 10, 2))
        var.set("The temperature in hyderabad is " + data + ' degrees celsius')
        window.update()
        speak("The temperature in hyderabad is " + data + 'degrees celsius')

        # speak(data)
        data = str(round((json_data['main']['feels_like']) / 10, 2))
        speak("Feel like" + data + 'degrees celsius')
        var.set("Feel like " + data + ' degrees celsius')
        window.update()
        speak("Have a great day ahead ")
        var.set("Have a great day ahead ")
        window.update()


    def Jokes():
        joke = pyjokes.get_joke('en', 'neutral')
        var.set(joke)
        window.update()
        speak(joke)


    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            var.set("Listening...")
            window.update()
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            var.set("Recognizing...")
            window.update()
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("User said: ", [query])

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query


    def syn():
        speak("Word please")
        word = takeCommand().lower()
        result = PyDictionary.synonym(word)
        result = result[0:3]
        var.set("The synonym of the " + word + " is " + str(result))
        window.update()
        speak("The synonym of the word is" + str(result))


    def any():
        speak("Word please")
        word = takeCommand().lower()
        if word is not None:
            result = PyDictionary.antonym(word)
            result = result[0:3]
            var.set("The antonym  of the "+word+" is " + str(result))
            window.update()
            speak("The antonym  of the word is" + str(result))


    def meanings():
        speak("Word please")
        word = takeCommand().lower()
        result = PyDictionary.meaning(word)

        var.set(result)
        window.update()
        speak("The meaning of the word is" + str(result))


    def Task():
        # btn2['state'] = 'disabled'
        # btn0['state'] = 'disabled'
        btn1.configure(bg='orange')

        # wishMe()
        while True:

            btn1.configure(bg='orange')
            query = takeCommand().lower()

            if 'hello' in query:
                var.set("hello")
                window.update()
                speak("hello")
            elif "calculate" in query:
                calci()


            elif 'translate' in query:
                Trans()


            elif 'downloading speed' in query:

                SpeedTest(query)


            elif 'uploading speed' in query:

                SpeedTest(query)

            elif 'internet speed' in query:
                SpeedTest(query)
            elif 'screenshot' in query:
                screenshot()
            elif 'battery percent' in query:
                Cpu_Battery()
            elif 'tell me a joke' in query:
                Jokes()

            elif 'temperature' in query:
                Temperature()

            elif 'open facebook' in query:
                openapps(query)

            elif 'location' in query:
                var.set("Ok mam This is your location")
                window.update()
                speak("Ok mam This is your location")
                webbrowser.open('https://www.google.co.in/maps/@17.3905892,78.4112494,13z?hl=en')

            elif 'news' in query:
                news()
            elif 'meaning' in query:
                meanings()
            elif 'opposite' in query:
                any()
            elif 'another' in query:
                syn()
            elif 'open adobe' in query:

                openapps(query)
            elif 'open notepad' in query:
                openapps(query)
            elif 'music' in query:
                Music()

            elif 'open code' in query:

                openapps(query)
            elif 'temperature' in query:
                Temperature()

            elif 'open google maps' in query:

                openapps(query)
            elif 'thanks for your help' in query:
                speak("It was great helping you out!")
                speak("Bye")
                var.set("It was great helping you out!")
                window.update()
                quit()


    def update(ind):
        frame = frames[ind % 100]
        ind += 1
        label.configure(image=frame)
        window.after(100, update, ind)


    label1 = Label(window, textvariable=var, bg='#32a89d')
    label1.config(font=("Arial", 20))
    var.set('Welcome')
    label1.pack()
    files = 'C:\\Users\\DELL\\PycharmProjects\\pythonProject2\\MINI PROEJCT\\assistantgif.py.gif'
    frames = [PhotoImage(file=files, format='gif -index %i' % (i)) for i in range(100)]
    window.title('Assistant')

    label = Label(window, width=600, height=600)
    label.pack()
    window.after(0, update, 0)

    btn0 = Button(text='WISH ME', width=50, command=wishMe, bg='#327da8')
    btn0.config(font=("Arial", 15))
    btn0.pack()
    btn1 = Button(text='PLAY', width=50, command=Task, bg='#327da8')
    btn1.config(font=("Arial", 15))
    btn1.pack()
    btn2 = Button(text='EXIT', width=50, command=window.destroy, bg='#327da8')
    btn2.config(font=("Arial", 15))
    btn2.pack()

    window.mainloop()
