import os
import subprocess as sub
import time
import speech_recognition as sr


def read_config():
    """
    Reads keywords and asociated commands from file in XDG_CONFIG_HOME
    Returns: [([keyword],command)]
    """

    def generate_keywords(words):
        return [(word, 1.0) for word in words]

    keywords = []
    commands = []
    path = "%s/voice-control/config" % os.environ['XDG_CONFIG_HOME']
    with open(path, "r") as config_file:
        for line in config_file:
            fields = line.split(sep=",")
            words = fields[0].split()
            commands.append((set(words), fields[1]))
            for word in words:
                keywords.append((word,1.0))
    
    print(commands)
    return commands,keywords



def listen(commands, keywords):
    """
    Listens to mic and executes commands associated with keywords
    """

    def callback(recognizer, audio):
        try:
            sentence = recognizer.recognize_sphinx(audio, keyword_entries=keywords)
            print("i understod: %s" % sentence)
            words = set(sentence.split())
            for (key, command) in commands:
                if len(key.intersection(words)) >= 1:
                    print(command)
                    sub.Popen(command, shell=True)

        except sr.UnknownValueError:
            print("i dont understand")
        except sr.RequestError as e:
            print("error sphinx {0}".format(e))

    r = sr.Recognizer()
    m = sr.Microphone()

    with m as source:
        r.adjust_for_ambient_noise(source)

        while True:
            audio = r.listen(source)
            callback(r, audio)


if __name__ == "__main__":
    commands,keywords = read_config()
    listen(commands, keywords)

