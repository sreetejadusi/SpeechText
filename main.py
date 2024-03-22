# import pyaudio
# import speech_recognition as sr
# import pyttsx3


# def main():
#     recognizer = sr.Recognizer()
#     while (1):

#         # Exception handling to handle
#         # exceptions at the runtime
#         try:

#             # use the microphone as source for input.
#             with sr.Microphone() as source2:
#                 recognizer.adjust_for_ambient_noise(source2)
#                 audio2 = recognizer.listen(source2)
#                 myText = recognizer.recognize_google(audio2)
#                 myText = myText.lower()

#                 print("Did you say ", myText)
#                 speak(myText)

#         except sr.RequestError as e:
#             print("Could not request results; {0}".format(e))

#         except sr.UnknownValueError:
#             print("unknown error occurred")


# def speak(command):
#     engine = pyttsx3.init('nsss', True)
#     engine.say(command)
#     engine.runAndWait()


# if __name__ == '__main__':
#     main()


