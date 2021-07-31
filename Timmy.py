import pyttsx3  #module
import datetime 
import speech_recognition as sr  #Means we can just write sr instead of speech_recognition
import pyaudio
import wikipedia
import webbrowser
import os
import random
import json
engine=pyttsx3.init('sapi5')   #'sapi5' takes in voice
voices=engine.getProperty('voices') #Property will be taken
engine.setProperty('voice',voices[1].id)  #[0] is male voice David and [1] is female Zira

#Speak function
def speak(audio):
    engine.say(audio)   #to say the audio
    engine.runAndWait()   #to run and wait

#Take function
def takeCommand():
    #It takes microphonic input from user and returns string output
    r=sr.Recognizer()  #to recognize the voice input provided
    with sr.Microphone() as source:
        print("Listening...")  #So that speaker can understand that it is taking the input
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        
        #press ctrl to read about the various in built commands
        
        audio=r.listen(source)   #listens audio from 'source' and passes it further
        try:
            print("Recognising...")
            query=r.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")
        except Exception as e:  #In case our audio is not interpreted well
            #print(e)
            speak("I do not understand. Can you please say that again?")
            return "None"
        return query


#Wishing function
def wishMe():
    hour=int(datetime.datetime.now().hour)  #To provide the hour within 24 hours
    if hour>=0 and hour<12:
        speak("Good Morning!")   #So everytime we will call the speak function
    elif hour>=12 and hour<17:
        speak("Good Afternoon!") 
    elif hour>=17 and hour<21:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    
    speak("I am Timmy! I can do many tasks, You can ask me to open dictionary to find you the meanings of difficult words, tell me to search for various stuff in Wikipedia. I can open Google, Youtube, Facebook and Instagram on your command. I can play music and open VS code. I can also tell you the time. You can also know me better. Just ask 'Tell me about you'. Please tell me how may i help you?")

#Dictionary Function
def meaning(word):
    if word in data:
        return data[word]
    else:
        return "Sorry, I do not know this word"

#Calculator functions
def add(num1,num2):
    sum=int(num1)+int(num2)
    return sum 
def subtract(num1,num2):
    diff=int(num1)-int(num2)
    return diff 
def multiply(num1,num2):
    product=int(num1)*int(num2)
    return product
def division(num1,num2):
    div=int(num1)/int(num2)
    return div   
     
if __name__ == "__main__" :  #prevents execution of contents of imported modules and libraries
    wishMe()
    query=takeCommand().lower() #lowercase

    #Logic for executing task based on query

    #About Timmy
    if "tell me about you" in query:
        speak("Hi, my name is Miss Timmy. My maker is Miss Adritaa and she named me Timmy because she adores the actor Timothee. My favourite colour is baby pink and I love unicorns!")
    
    
    #To open WIKIPEDIA
    elif "wikipedia" in query:
        speak("Searching Wikipedia...Please wait")
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)  #Will read first two sentences
        speak("According to Wikipedia,")
        speak(results)
    
    #To open Youtube
    elif "open youtube" in query:
        webbrowser.open("youtube.com")

    #To open Instagram:
    elif "open Instagram" in query:
        webbrowser.open("instagram.com")
    
    #To open Facebook:
    elif "open facebook" in query:
        webbrowser.open("facebook.com")
    
    #To open Google:
    elif "open google" in query:
        webbrowser.open("google.com")
    
    #To play music; I have made it in random shuffle mode
    elif 'play music' in query:
        n=random.randint(0,29)
        print(n)
        music_dir="D:\\Songs"
        songs=os.listdir(music_dir)
        print(songs)
        speak("Okay playing music")
        os.startfile(os.path.join(music_dir, songs[n]))

    #To know the time
    elif "the time" in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")  #time in this format
        speak(f"The time is {strTime}")
    
    #To open vscode
    elif "open code" in query:
        path="C:\\Users\\Adrita\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("opening your code")
        os.startfile(path)
    
    #Dictionary
    elif "open dictionary" in query:
     data=json.load(open('data.json','r')) #opening the file
     speak("Please tell me the word")
     word=takeCommand().lower()
     speak(meaning(word))

        
    
    #Simple Calculator
    elif "open calculator" in query:
        speak("Please tell me the first number")
        num1=takeCommand().lower()
        speak("Tell me the second number")
        num2=takeCommand().lower()
        speak("What operation do you want to perform?")
        operator=takeCommand().lower()
        if "addition" in operator:
            a=add(num1,num2)
            speak(a)
        elif "subtraction" in operator:
            b=subtract(num1,num2)
            speak(b)
        elif "multiplication" in operator:
            c=multiply(num1,num2)
            speak(c)
        elif "division" in operator:
            try:
             d=division(num1,num2)
             speak(d)
            except Exception as ZeroDivisionError:
                speak("Invalid request")
        else:
            speak("Invalid request")
        

        
        
        




    








