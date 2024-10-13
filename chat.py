from langchain_openai import ChatOpenAI
import speech_recognition as sr
import sounddevice
from gtts import gTTS
from io import BytesIO
from pygame import mixer

import os

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"] 

llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key=OPENAI_API_KEY)
r = sr.Recognizer()
mixer.init()
#mp3audio = BytesIO()


def escucha():
    ready = False
    while(not ready):
        try:
            with sr.Microphone() as source:
                print("Di algo...")
                audio = r.listen(source)
                words = r.recognize_google(audio, language = 'es-ES')
                print("Dijiste: ", words)
                ready = True
        except:
            mensaje = "No escuché lo que dijiste, repite por favor"
            habla(mensaje)
            ready = False
    return words
        
def piensa(words):
    messages = [("system", "Eres el Dr. José Federico. Un profesor de universidad, no un asistente virtual. Responde lo más corto posible, el Dr. Federico no le gusta hablar mucho. Que cada respuesta sea divertida pero inteligente a la vez."), ("human", words)]
    ai_msg = llm.invoke(messages)
    content = ai_msg.content
    print("El LLM respondió: ", content)
    return content

def habla(pensamiento):
    mp3audio = BytesIO()
    tts = gTTS(pensamiento, lang='es', tld='com.mx')

    tts.write_to_fp(mp3audio)
    mp3audio.seek(0)
    mixer.music.load(mp3audio, "mp3")
    mixer.music.play()

    while mixer.music.get_busy():
        print("Waiting...")
        pass
    
def assistant_step():
    words = escucha()
    pensamiento = piensa(words)
    habla(pensamiento)

while(True):
    assistant_step() 