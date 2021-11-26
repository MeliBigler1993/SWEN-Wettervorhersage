"""
contains functions for text-to-speech and speech-to-text
"""
import pyttsx3
import speech_recognition as sr

class Speaker():
    """
    initiates a Speaker that can listen and speak to the user \\
    :lang: str ('de' || 'en') - sets the language of the speaker
    """
    def __init__(self, lang='de'):
        self.voice = pyttsx3.init()
        self.voice.setProperty('volume', 0.2)
        if lang == 'de':
            self.voice.setProperty('voice', 'com.apple.speech.synthesis.voice.anna.premium')
        if lang == 'en':
            self.voice.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
        self.rec = sr.Recognizer()

    def listen_for_input(self):
        """
        :return: voice_input - the input the user gave
        """
        with sr.Microphone() as mic:
            print("Ich höre zu...")
            audio_text = self.rec.listen(mic)
            voice_input = self.rec.recognize_google(audio_text, language="de-DE")
            print("Danke. Du nanntest:", voice_input)
            return voice_input

    def speak(self, text):
        """
        speaks a text \\
        :text: str - the text that should be spoken
        """
        self.voice.say(text)
        self.voice.runAndWait()
