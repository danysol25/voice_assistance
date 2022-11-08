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

transformar_audio_en_texto()