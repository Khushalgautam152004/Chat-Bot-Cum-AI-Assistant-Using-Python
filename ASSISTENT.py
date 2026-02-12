import pyttsx3
from datetime import datetime

engine= pyttsx3.init()
engine.setProperty('rate', 140)
def speak(text):
    print("AI BOT :", text)
    
    for line in text.split("."):
       if line.strip():
           
            engine.runAndWait()
    engine.say(text)
    

print("Khushal : Hello ! I am a AI Assistant . type exit to end.\n  ")

while True:
          user_input= input("You:").lower()
          

          if "exit" in user_input:
           speak("Goodbye Khushal, have a nice day!")
           break

          if"hello" in user_input or "hi" in user_input:
            speak("Hello i m Khushal how can i assist you ?")

          elif "how are you" in user_input:
             speak(" i am just a code but i feel awesome helping you")

          elif "name" in user_input:
             speak(" i am khushal your python ai assistant")

          elif "time" in user_input:
             current_time = datetime.now().strftime("%H:%M:%S")
             speak(current_time)


          elif "calculate" in user_input:
             try:
                result = eval(user_input.replace("calculate",""))
                speak(f"this is result {result} ")
             except:
                speak("sorry i couldn't understand the calculation ")


