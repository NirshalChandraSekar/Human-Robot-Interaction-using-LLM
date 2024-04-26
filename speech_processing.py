import speech_recognition as sr
import pyttsx3

class speech_processing:

    def __init__(self):
        self.input_speech = None
        self.input_text = ""
        self.output_text = None
        self.output_speech = None
        self.r = sr.Recognizer()

    def record_audio(self):
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source, duration=1)
            print("Recording started (you have 20 seconds to tell what you need)")
            self.input_speech = self.r.listen(source, timeout=20)
            print("Recording completed")

    def speech_to_text(self):
        self.record_audio()
        try:
            print("Recognizing text from the audio")
            self.input_text = self.r.recognize_google(self.input_speech)
        except Exception as ex:
            print(ex)
        return self.input_text
    
    def text_to_speech(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()


if __name__ == "__main__":
    process_audio = speech_processing()
    
    input_text = process_audio.speech_to_text()
    print(input_text)

    text = "this is a test text"
    process_audio.text_to_speech(input_text)
    
    