import pyttsx3

engine = pyttsx3.init()
my_file = open("text.txt","r")
text = my_file.read()
engine.say(text)
engine.runAndWait()