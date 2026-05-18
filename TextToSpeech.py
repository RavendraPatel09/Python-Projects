import pyttsx3
engine = pyttsx3.init()
text = input("Enter text: ")
engine.say(text)
engine.runAndWait()