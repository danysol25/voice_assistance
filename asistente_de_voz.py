import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance
import pyjokes
import webbrowser
import datetime
import wikipedia

#escuchar nuestro micrófono y devolver audio como texto
def transformar_audio_en_texto():
    #almacenar recognizer en var
    r = sr.Recognizer()

    #config micrófono
    with sr.Microphone() as origen:
        #tiempo de espera desde que se activa al micrófono, hasta q empieza a escuchar
        r.pause_threshold=0.8

        #informar que comenzó la grabación
        print('Comienza a hablar...')

        #guardar el audio dentro de var
        audio = r.listen(origen)

        #contención de errores inesperados
        try:
            #buscar en google lo que haya escuchado
            pedido = r.recognize_google(audio, language='es-ar')

            #imprimir lo transformado en texto
            print('Dijiste: ' + pedido)

            #devuelve el pedido
            return pedido

        #en caso de que no comprenda el audio
        except sr.UnknownValueError:
            #prueba de q no comprendió el audio
            print('El audio no fue claro.')

            #devolver error
            return 'Sigo esperando...'

        #en caso de q pudo grabar el audio, pero no lo puede transformar en str
        except sr.RequestError:
            #prueba de q no comprendió el audio
            print('No hay servicio.')

            #devolver error
            return 'Sigo esperando...'

        #en caso de otro error inesperado
        except:
            #prueba de q no comprendió el audio
            print('Algo ha salido mal')

            #devolver error
            return 'Sigo esperando...'
#función para que el asistente sea escuchado

def hablar(mensaje):

    #encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"

#informar el día de la semana
def pedir_dia():
    #datos de hoy
    dia = datetime.date.today()
    print(dia)
    dia_semana = dia.weekday()
    #diccionario con nombre de días
    calendario = {0:'Monday',
                  1:'Tuesday',
                  2: 'Wednesday',
                  3: 'Thursday',
                  4: 'Friday',
                  5: 'Saturday',
                  6: 'Sunday'}
    hablar(f'Today is {calendario[dia_semana]}')

#informar la hora
def pedir_hora():
    hora = datetime.datetime.now()
    hora = f'In this moment, the hour is {hora.hour}, with {hora.minute} minutes and {hora.second} seconds.'
    print(hora)
    #decir la hora
    hablar(hora)

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

def pedir_cosas():
    #activar saludo inicial
    saludo_inicial()

    #loop para q siga funcionando hasta q decidamos terminarlo nosotros
    comenzar = True
    
    #loop central
    while comenzar:
        #activar micrófono y guardar el pedido en str
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Opening Youtube...')
            webbrowser.open('https://www.youtube.com/')
            continue
        elif 'abrir navegador' in pedido:
            hablar("Sure, I'll open the browser")
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'qué día es' in pedido:
            pedir_dia()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Looking for that in wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('en')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia says this: ')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('looking in internet...')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('This is what I found...')
            continue
        elif 'reproducir' in pedido:
            hablar('Great idea, I will play it')
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL', 
                       'amazon':'AMZN',
                       'google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yfinance.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(F'Found it! The price of {accion} is {precio_actual}')
                continue
            except:
                hablar('Sorry, I couldnt find it.')
                continue
        elif 'adiós' in pedido:
            hablar('Perfect. It was a pleasure to help.')
            break
pedir_cosas()