import speech_recognition as sr
from word2number import w2n

keywords = {
    "delete all" : "delete_all",
    "delete line" : "delete_line",
    "delete" : "delete",
    "new line" : "new_line"
}

# number_map = {
#     "zero" : 0,
#     "one" : 1,
#     "two" : 2,
#     "three" : 3,
#     "four" : 4,
#     "five" : 5,
#     "six" : 6,
#     "seven" : 7,
#     "eight" : 8,
#     "nine" : 9,
# }

class AnalyzeTextToCode:
    def analyze(script_code, speech):
        for keyword in keywords.keys():
            if keyword in speech:
                return getattr(AnalyzeTextToCode, keywords[keyword])(script_code, speech)

    def delete_line(script_code, speech):
        if "number" in speech:
            position_of_text_number = speech.rfind('number') + len("number") + 1
            try:
                if type(int(speech[position_of_text_number])) == int:
                    line_number = int(speech[position_of_text_number])
            except:
                number_in_text = speech[position_of_text_number : ]
                #line_number = number_map[number_in_text]
                line_number = w2n.word_to_num(number_in_text)
            script_code = script_code.split("\n")
            if len(script_code) < line_number:
                print("Error: Line Number to delete exceeds the total lines in code.")
            else:
                script_code.pop(line_number-1)
            return "\n".join(script_code)
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

    def new_line(script_code, speech):
        script_code = script_code + '\n'
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



script_code = "print(\"Hello World1\")\nprint(\"Hello World2\")\nprint(\"Hello World3\")\nprint(\"Hello World4\")\nprint(\"Hello World5\")\nprint(\"Hello World6\")"
#speech = SpeechToTextEngine.recognize_voice()
speech = "add new line"

print(AnalyzeTextToCode.analyze(script_code, speech))
