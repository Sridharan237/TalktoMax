#TALK TO MAX ---> VIRTUAL ASSISTANT
import tkinter as tk                                            #tkinter -> is for creating gui (front end)                                 
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import time as tm
import wikipedia
import pyjokes

#front end - tkinter
def tkinter_execute():
    win = tk.Tk(className=" VIRTUAL ASSISTANT")
    win.geometry("600x550")
    win.configure(background="white")
    
    label=tk.Label(text="TALK WITH MAX !!!",background="white")
    global text
    text=tk.Text(height=20,width=50,border=6,relief="groove",background="black",foreground="white")              # or height = 10

    Start=tk.Button(text="start",activebackground="yellow",command=run_max)
    Exit=tk.Button(text="exit",command=win.destroy,activebackground="yellow")
    Clear=tk.Button(text="clear",command=clearText,activebackground="yellow")
    
    label.pack()                          # Packing all the widgets or buttons on to the tkinter gui or tkinter window
    text.pack()                 
    Start.pack()
    Exit.pack()
    Clear.pack()

def clearText():                           #To make the Clear BUTTON functionable and runs when Clear button is pressed or clicked or onclick
    text.delete("1.0","end")

def textInsertion(message):                #To add or write the plain text to the text widget in tkinter window
    text.insert(tk.END,message)
    
#Back end - speech recognition
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(Text):
    engine.say(Text)
    engine.runAndWait()
 
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            text.insert(tk.INSERT,"listening..."+"\n")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower() 
            if 'max' in command:
                command = command.replace('max', '')
                print(command)
    except UnboundLocalError:
        pass
    return command

def run_max():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '') 
        message1='playing ' + song +'\n'
        textInsertion(message1)
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        message2='Current time is ' + time+'\n'
        textInsertion(message2)
        talk('Current time is ' + time)
    elif 'tell about' in command:
        person = command.replace('tell about', '') 
        info = wikipedia.summary(person, 1)
        textInsertion(info)
        print(info)
        talk(info)
    elif 'angry' in command:
        message3='sorry, I can\'t help you'+'\n'
        textInsertion(message3)
        talk('sorry, I can\'t help you')
    elif 'how are you' in command:
        message4='I am fine. And hope you fine'+'\n'
        textInsertion(message4)
        talk('I am fine. And hope you fine')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        message5='Please say the command again.'+'\n'
        textInsertion(message5)
        talk('Please say the command again.')


tkinter_execute()               #To open tkinter gui ---> for to look like a front end application
