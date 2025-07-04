import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import os

id1 = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
id2 = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-ES_HELENA_11.0"
id3 = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-MX_SABINA_11.0"
# heard our mic
def change_audio_to_text():


    #storage recognizer to a variable
    r = sr.Recognizer()

    #config  mic
    with sr.Microphone() as origen:


        # info the start of rec
        print("Ya puedes hablar")
        audio = r.listen(origen)

        try:

            #search in google
            r.pause_threshold = 0.8
            p = r.recognize_google(audio,language='es-mx')

            #proof that the search was succesful
            print("Dijiste: "+ p)

            return p
        # in case of none of audio
        except sr.UnknownValueError:

            #proof of the error
            print("Upss, No entendí")
            # return error
            return "Estoy esperando"
        #in case of didnt work
        except sr.RequestError:

            #proof of the error
            print("Upss, No entendí")
            # return error
            return "Estoy esperando"
        except:
            #proof of the error
            print("Upss, No entendí")
            # return error
            return "Estoy esperando"
        
# texto to audio from the assistant
def change_texto_to_audio(mensaje):

    #power on the engine of pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice',id3)
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
    calendar = {0:'Lunes',
                1:'Martes',
                2:'Miércoles',
                3:'Jueves',
                4:'Viernes',
                5:'Sábado',
                6:'Domingo'}
    month = {1:'enero',2:'febrero',3:'marzo',4:'abril',5:'mayo',
             6:'junio',7:'julio',8:'agosto',9:'septiembre',10:'octubre',
             11:'noviembre',12:'diciembre'}
    change_texto_to_audio(f'Hoy es {calendar[day_week]}, {day.day} de {month[day.month]} del {day.year}')

#say the hour of the day
def say_hour():

    #create variable with data of the hour
    hour = datetime.datetime.now()
    hour = f'Ahora mismo, La hora es {hour.hour} horas con {hour.minute} minutos y {hour.second} segundos'
    print(hour)
    change_texto_to_audio(hour)

def official_grettings():
    #create variable with data of hour
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour > 19:
        moment = 'Buenas noches'
    elif hour.hour >= 6 and hour.hour < 12:
        moment = 'Buenos días'
    else:
        moment = 'Buenas tardes'
    #Say the gretting
    change_texto_to_audio(f"{moment}, Soy Sara, tu asistente personal, pideme cualquier cosa")

def ask_something():

    #active initial greetting
    official_grettings()

    #cut variable
    start = True
    
    #central loop

    while start:

        #start the micro and save the ask in a string
        ask = change_audio_to_text().lower()
        
        if 'abre youtube' in ask:
            change_texto_to_audio('Ok, abriendo youtube')
            webbrowser.open("https://www.youtube.com/")
            continue
        elif 'abre brave' in ask:
            change_texto_to_audio('ok, abriendo brave')
            webbrowser.open('https://www.google.com')
            continue
        elif 'abre chat gpt' in ask:
            change_texto_to_audio('ok, abriendo chatgpt')
            webbrowser.open('https://www.chatgpt.com')
            continue
        elif 'abre visual studio' in ask:
            change_texto_to_audio("Ok, abriendo Visual Studio")
            os.system('"C:\\Users\\pablo\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code.exe"')
            continue
        elif "abre minecraft" in ask:
            change_texto_to_audio("ok, abriendo Minecraft")
            os.system('"C:\\XboxGames\\Minecraft Launcher\\Content\\gamelaunchhelper.exe"')
            continue
        elif "abre valorant" in ask:
            change_texto_to_audio("ok, abriendo valorant")
            os.system('"C:\\Riot Games\\VALORANT\\live\\VALORANT.exe')
            continue
        elif 'qué día es hoy' in ask:
            day_week()
            continue
        elif 'qué hora es' in ask:
            say_hour()
            continue
        elif 'busca en wikipedia' in ask:
            change_texto_to_audio('Buscando en wikipedia...')
            ask  = ask.replace('busca en wikipedia','')
            try:
                wikipedia.set_lang('es')
                result = wikipedia.summary(ask,sentences=1)
                change_texto_to_audio('Wikipedia encontró esto: ')
                change_texto_to_audio(result)
            except:
                change_texto_to_audio('Lo siento, no encontré eso')
            continue
        elif 'busca en google' in ask:
            ask = ask.split('google')[-1:-1:]
            pywhatkit.search(ask)
            change_texto_to_audio('Esto es lo que encontré')
            continue
        elif 'reproduce' in ask:
            change_texto_to_audio('ok, reproduciendo')
            pywhatkit.playonyt(ask)
            continue
        elif 'broma' in ask:
            change_texto_to_audio(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acción' in ask:
            action = ask.split('acción')[-1].strip()
            bill = {'fibramonterrey':'FMTY14','ivvpeso':'IVVPESO'}
            try:
                action_search = bill[action]
                action_search = yf.Ticker(action_search)
                price = action_search.info['regularMarketPrice']
                change_texto_to_audio(f'Lo encontré, El precio de {action} es {price}')
                continue
            except:
                change_texto_to_audio('Lo siento no lo encontré')
        elif 'adiós' in ask:
            change_texto_to_audio('Nos vemos Juan, Ten un lindo día') 
            break



ask_something()


# engine = pyttsx3.init()

# for v in engine.getProperty('voices'):
#     print(v)
# # idiom options

