import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

id1 = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
id2 = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-ES_HELENA_11.0"
# heard our mic
def change_audio_to_text():


    #storage recognizer to a variable
    r = sr.Recognizer()

    #config  mic
    with sr.Microphone() as origen:


        # info the start of rec
        print("you can already speak")
        audio = r.listen(origen)

        try:

            #search in google
            r.pause_threshold = 0.8
            p = r.recognize_google(audio,language='en-us')

            #proof that the search was succesful
            print("You say: "+ p)

            return p
        # in case of none of audio
        except sr.UnknownValueError:

            #proof of the error
            print("Upss, i dont understand")
            # return error
            return "i still waiting"
        #in case of didnt work
        # except sr.RequestError:

        #     #proof of the error
        #     print("Upss, there is not service")
        #     # return error
        #     return "i still waiting"
        # except:
        #     print(except
        #     #proof of the error
        #     print("Upss, something went wrong")
        #     # return error
        #     return "i still waiting"
        
# texto to audio from the assistant
def change_texto_to_audio(mensaje):

    #power on the engine of pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice',id1)
    #say the message
    engine.say(mensaje)
    engine.runAndWait()

#say the day of the week
def day_week():

    #create variable with data of today
    day = datetime.date.today()
    print(day)
    day_week = day.weekday()
    
    #dictionary of days
    calendar = {0:'Monday',
                1:'Tuesday',
                2:'Wednesday',
                3:'Thursday',
                4:'Friday',
                5:'Saturday',
                6:'Sunday'}
    change_texto_to_audio(f'Today is {calendar[day_week]}')

#say the hour of the day
def say_hour():

    #create variable with data of the hour
    hour = datetime.datetime.now()
    hour = f'Right now, the time is {hour.hour} hours with {hour.minute} minutes and {hour.second} seconds'
    print(hour)
    change_texto_to_audio(hour)

def official_grettings():
    #create variable with data of hour
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour > 19:
        moment = 'Good night'
    elif hour.hour >= 6 and hour.hour < 12:
        moment = 'Good morning'
    else:
        moment = 'Good afternoon'
    #Say the gretting
    change_texto_to_audio(f"{moment}, I'm Sara, your personal assistant. Please, tell me how can i help you")

def ask_something():

    #active initial greetting
    official_grettings()

    #cut variable
    start = True
    
    #central loop

    while start:

        #start the micro and save the ask in a string
        ask = change_audio_to_text().lower()
        
        if 'open youtube' in ask:
            change_texto_to_audio('Ok, opening Youtube')
            webbrowser.open("https://www.youtube.com/")
            continue
        elif 'open browser' in ask:
            change_texto_to_audio('Ok, opening brave')
            webbrowser.open('https://www.google.com')
            continue
        elif 'day of the week' in ask:
            day_week()
            continue
        elif 'what time is it' in ask:
            say_hour()
            continue
        elif 'search in wikipedia' in ask:
            change_texto_to_audio('Searching that in wikipedia')
            ask  = ask.replace('search in wikipedia','')
            try:
                result = wikipedia.summary(ask,sentences=1)
                change_texto_to_audio('Wikipedia found this: ')
                change_texto_to_audio(result)
            except:
                change_texto_to_audio('Sorry i did not found that')
            continue
        elif 'search in google' in ask:
            ask = ask.replace('search in google','')
            pywhatkit.search(ask)
            change_texto_to_audio('This is what i have found: ')
            continue
        elif 'play' in ask:
            change_texto_to_audio('ok, starting to play')
            pywhatkit.playonyt(ask)
            continue
        elif 'joke' in ask:
            change_texto_to_audio(pyjokes.get_joke('en'))
            continue
        elif 'price of actions' in ask:
            action = ask.split('of')[-1].strip()
            bill = {'fibra monterrey':'FMTY14','ivvpeso':'IVVPESO'}
            try:
                action_search = bill[action]
                action_search = yf.Ticker(action_search)
                price = action_search.info['regularMarketPrice']
                change_texto_to_audio(f'I found it, the price of {action} is {price}')
                continue
            except:
                change_texto_to_audio('Sorry i did not found that')
        elif 'bye' in ask:
            change_texto_to_audio('Bye Juan, have a nice day') 
            break


ask_something()




# for v in engine.getProperty('voices'):
#     print(v)
# idiom options

