import speech_recognition as sr

class SpeechToTextEngine:
    
    def recognize_voice():
        mic = sr.Microphone()
        recognize  = sr.Recognizer()

        while True:
            with mic as source:
                recognize.adjust_for_ambient_noise(source)
                audio = recognize.listen(source)

            try:
                transcript = recognize.recognize_google(audio)
                print (transcript)
                return transcript
                #logging.info(transcript)
            except sr.RequestError:
                print ('API Error')
                continue
            except sr.UnknownValueError:
                print ('Unable to recognize speech')
                print ('Looks like you are smarter than the Computer.!!! 🧠')
                continue  