print("Hello world")
import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source :
        print("Listening....")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()

        if "my friend" :
            print(command)
except:
    print("I have failed")