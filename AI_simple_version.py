import pyttsx3
import speech_recognition
from datetime import date, datetime


# Voice Recognition: Android will listen and print out the words that we spoke to it

android_ear = speech_recognition.Recognizer()
android_mouth = pyttsx3.init()
android_brain = ''

while True: 
    with speech_recognition.Microphone() as mic:
        print('Android: I\'m Listening')
        audio = android_ear.listen(mic)

    print('Android...')

    try:    
        you = android_ear.recognize_google(audio)
    except:
        you = ''


    if you == '':
        android_brain = 'I can\'t hear you'
    elif 'hello' in you:
        android_brain = 'Hello. My name is XRoid. How can I help you?' 
    elif 'today' in you:
        today = date.today()
        android_brain = today.strftime('%B %d, %Y')
    elif 'time' in you:
        android_brain = datetime.now()
    elif 'Thanksgiving' in you:
        android_brain = 'Thu, Nov 28, 2024'
    elif 'Christmas' in you:
        android_brain = 'Wed, Dec 25, 2024'
    elif 'daylight':
        android_brain = 'Sun, Mar 10, 2024 – Sun, Nov 3, 2024'
    elif 'bye' in you:
        android_brain = 'Bye. See you later!'
        android_mouth.say(android_brain)
        android_mouth.runAndWait()
        break
    else:
        android_brain = 'I\'m fine. Thank you. And you?'

    
    print('Android: ' + android_brain)

    # Android will respond to you
    android_mouth.say(android_brain)
    android_mouth.runAndWait()