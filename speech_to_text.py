import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import time
import numpy as np


def timer(duration):
    while duration:
        mins, secs = divmod(duration, 60)
        sec_timer = f"{mins} mins:{secs} seconds Left"
        print(sec_timer, end=" \r")
        time.sleep(1)
        duration -= 1


def record_audio(filename):
    fs = 44100
    duration = 10

    print("Recording..........")

    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)

    timer(duration)
    sd.wait()

    data = (np.iinfo(np.int32).max * (myrecording/np.abs(myrecording).max(
    ))).astype(np.int32)
    write(filename, fs, data)


filename = "new_record.mp3"


def speech_to_text(file):
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = r.record(source)

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("could not understand audio")
        return ""
    except sr.RequestError:
        print("Network error")
        return ""


record_audio(filename)
text = speech_to_text('new_record.mp3')
print(text)