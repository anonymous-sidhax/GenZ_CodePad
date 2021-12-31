import speech_recognition as sr

keywords = {
    "delete" : "delete_line"
}

class AnalyzeTextToCode:
    def analyze(speech):
        if speech in keywords.keys():
            return getattr(AnalyzeTextToCode, keywords[speech])(script_code)

    def delete_line(script_code):
        position_of_next_line = script_code.rfind('\n')
        if (position_of_next_line > 0):
            script_code = script_code[ : position_of_next_line] + "\n"
        return script_code

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
                #logging.info(transcript)
            except sr.RequestError:
                print ('API Error')
                continue
            except sr.UnknownValueError:
                print ('Unable to recognize speech')
                print ('Looks like you are smarter than the Computer.!!! 🧠')
                continue  

#SpeechToTextEngine.recognize_voice()

script_code = "print(\"Hello World\")\nprint(\"Hello World\")\nprint(\"Hello World\")"
speech = "delete"

print(AnalyzeTextToCode.analyze(speech))