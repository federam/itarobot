# Reconocimiento de Voz usando un archivo .wav

import speech_recognition as sr

r = sr.Recognizer()

salud2 = sr.AudioFile('saludos.wav')
with salud2 as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)

L = r.recognize_google(audio, language= 'es-MX')
print(L)

test = L.split()
print("Separando las palabras")
print(test)
print(type(test))

palabras = ['saludos','México','Mundo']
if any(palabra in test for palabra in palabras):
   print("Son saludos")

import re
re.findall(r'saludos|México',L)