import pyaudio
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('nsss', True)
engine.say(input())
engine.runAndWait()
