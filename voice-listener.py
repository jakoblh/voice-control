import os

import speech_recognition as sr

def generate_keywords(words):
    return [(word, 1.0) for word in words]


r = sr.Recognizer()
with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)


try:
    keywords = ["github", "firefox"]
    print("you said: " + \
            r.recognize_sphinx(audio, \
            keyword_entries=generate_keywords(keywords)))
except sr.UnknownValueError:
    print("could not understand anything")
except sr.RequestError as e:
    print("error; {0}".format(e))



