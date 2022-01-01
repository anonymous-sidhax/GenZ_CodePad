from mainApp.engine.speech_to_text import SpeechToTextEngine

keywords = {
    "delete all" : "delete_all",
    "delete line" : "delete_line",
    "delete" : "delete",
    "new line" : "new_line"
}


class Processor:
    def init(self):
        self.speech = SpeechToTextEngine()

    def run(self, script_code):
        speech = self.speech.recognize_voice()
        self.analyze(script_code, speech)
        
    def analyze(self, script_code, speech):
        for keyword in keywords.keys():
            if keyword in speech:
                return getattr(self, keywords[keyword])(script_code, speech)