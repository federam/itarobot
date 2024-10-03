'''
    Description: Create your own virtual assistant with python.
    Author: aulerjbailey
    Version: 1.0.0
    Video: https://youtu.be/8WKjX0dbh4E
'''
import speech_recognition as sr

import datetime

# name of the virtual assistant
name = 'cortana'

# the flag help us to turn off the program
flag = 1

listener = sr.Recognizer()

#engine = pyttsx3.init()

# get voices and set the first of them
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)

# editing default configuration
#engine. setProperty('rate', 178)
#engine.setProperty('volume', 0.7)

def listen():
    '''
        The program recover our voice and it sends to another function
    '''
    flag = 1
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            
            if name in rec:
                rec = rec.replace(name, '')
                flag = run(rec)
            else:
                #talk("Vuelve a intentarlo, no reconozco: " + rec)
                print("Vuelve a intentarlo, no reconozco: " + rec)
    except:
        pass
    return flag

def run(rec):
    '''
        All the actions that virtual assistant can do
    '''
    if 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        print("Son las " + hora)
    elif 'salir' in rec:
        flag = 0
        print("Saliendo...")
    else:
        print("Vuelve a intentarlo, no reconozco: " + rec)
    return flag

while flag:
    flag = listen()