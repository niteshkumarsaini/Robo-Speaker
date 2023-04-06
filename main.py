from win32com.client import Dispatch
speaker=Dispatch("SAPI.SpVoice")
print("Welcome to RoboSpeaker 2.0 Created by Nitesh.")
while True:
    x=input("What do you want me to Speak.. ")
    if(x=="exit"):
        print("Ok Bye....")
        speaker.Speak("Ok Byee.....")
        break
    speaker.Speak(x)
    
