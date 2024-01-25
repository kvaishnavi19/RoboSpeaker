import pyttsx3
print("Welcome to RoboSpeaker created by Vaishnavi")
while True:
    engine = pyttsx3.init()
    x = input("What do you want me to speak:")
    if x == 'q':
        engine.say("Goodbye!")
        engine.runAndWait()
        break
    engine.say(x)
    engine.runAndWait()
