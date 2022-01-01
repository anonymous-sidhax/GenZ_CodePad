import speech_recognition as sr

keywords = {
    "delete all" : "delete_all",
    "delete line" : "delete_line",
    "delete" : "delete"
}

class AnalyzeTextToCode:
    def analyze(speech):
        for keyword in keywords.keys():
            if keyword in speech:
                return getattr(AnalyzeTextToCode, keywords[keyword])(script_code, speech)

    def delete_line(script_code, speech):
        if "number" in speech:
            position_of_number = script_code.rfind('number') + len("number")
            print (position_of_number)
            return speech[position_of_number + 1]
        else:
            position_of_next_line = script_code.rfind('\n')
            if (position_of_next_line > 0):
                script_code = script_code[ : position_of_next_line] + "\n"
            return script_code
    
    def delete_all(script_code, speech):
        script_code = ""
        return script_code
    
    def delete(script_code, speech):
        script_code = script_code[ : len(script_code)-1]
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
                return transcript
                #logging.info(transcript)
            except sr.RequestError:
                print ('API Error')
                continue
            except sr.UnknownValueError:
                print ('Unable to recognize speech')
                print ('Looks like you are smarter than the Computer.!!! 🧠')
                continue  



script_code = "print(\"Hello World\")\nprint(\"Hello World\")\nprint(\"Hello World\")"
speech = SpeechToTextEngine.recognize_voice()

print(AnalyzeTextToCode.analyze(speech))