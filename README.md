# Introduction

A voice assistant that executes shell scripts associated with voice commands.\
Its uses sphinx to recognize words.\
Hence you can use it offline and no google employee will hear you whisper `firefox` to your computer.

# Usage

Note that ven I wouldn't recomend using `voice-control` right now.\
You are still welcome to play with it though.\
Anyways here's how to use it:

## Prequisits

For voice-control to work you need `SpeechRecognition`, `PyAudio` and `pocketsphinx`.\
Feel free to use `install.sh` to install the required packages.

## Usage

Before running voice-control you'll need to associate words with shell commands.\
Those are configured in `$XDG_CONFIG_HOME/voice-control/config`
Enter your words and commands in the following format: `[space sep. words],[shell command]`.\
You can also look into `config.example` for reference.

After setting up some voice commands you can finally run the service with `python voice-listener.py`

