import speech_recognition as sr


r = sr.Recognizer()
m = sr.Microphone()

with m as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    sentence = r.recognize_sphinx(audio)
    print("i understod: %s" % sentence)
except sr.UnknownValueError:
    print("i dont understand")
except sr.RequestError as e:
    print("error sphinx {0}".format(e))

