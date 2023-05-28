import pyttsx3
import wikipedia
#import pythoncom
#import pywin32
my_voice = pyttsx3.init()
In = input("Searhing wikipedia/google: ")
result = wikipedia.summary(In, sentences = 3)
print(result)
my_voice.say(result)
my_voice.runAndWait()
