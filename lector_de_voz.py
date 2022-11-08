import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance
import pyjokes
import webbrowser
import datetime
import wikipedia



def hablar(mensaje):

    #encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

#AJUSTAR IDIOMA
#engine = pyttsx3.init()
#engine.setProperty('voice', id1)

#for voz in engine.getProperty('voices'):
#    print(voz)

id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"

hablar('Hi Dani, hope you have a wonderful day.')

#informar el día de la semana
def pedir_dia():
    #datos de hoy
    dia = datetime.date.today()
    print(dia)
    dia_semana = dia.weekday()
    #diccionario con nombre de días
    calendario = {0:'Lunes',
                  1:'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    hablar(f'Today is {calendario[dia_semana]}')

pedir_dia()

#informar la hora
def pedir_hora():
    hora = datetime.datetime.now()
    hora = f'In this moment, the hour is {hora.hour}, with {hora.minute} minutes and {hora.second} seconds.'
    print(hora)
    #decir la hora
    hablar(hora)

pedir_hora()

#saludo INICIAL
def saludo_inicial():
    #crear variable con datos hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Good night'
    elif hora.hour >= 6 and hora.hour <= 12: #también es lo mismo que escribir: elif 6 <= hora.hour > 12:
        momento = 'Good morning'
    else:
        momento = 'Good afternoon'

    hablar(f"{momento}! I'm Zira, your assistant. How can I help you?")

saludo_inicial()