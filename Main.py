import os
import time
#Using the below libraries to import sound
import pyaudio
import playsound
#Using google text to speech
from gtts import gTTS
#importing open ai to use our AI key
import openai
import speech_recognition as sr
import pyautogui

import pytesseract
#import PIL import Image

api_key = 'sk-proj-FnK3MkwZfg7CROBpXm1tT3BlbkFJwJSbLwKTm50P2rtCaCoJ'

lang = 'en'

openai.api_key = api_key

guy = ''
#Set up the microphone since we are using the internal speaker of the computer it is 0
microphone = sr.Microphone(device_index=0)

def play_audio(text):
    """This function is used to play back the text in our speech"""
    speech = gTTS(text=text, lang = lang, slow=False, tld = 'com.au')
    speech.save('output.mp3')
    playsound.playsound('output.mp3')

def get_audio():
    r = sr.Recognizer()
    with microphone as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
            global guy
            guy = said

            if 'my boyfriend' in said:
                play_audio('I love you very much')

        except Exception as e:
            print('Exception', str(e))

while True:
    if 'stop' in guy:
        break
    get_audio()


