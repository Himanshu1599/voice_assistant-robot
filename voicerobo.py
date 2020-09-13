#pip install pipwin
#pipwin install pyttsx3
import pyttsx3 
import datetime
#pip install speechRecognition
import speech_recognition as sr
#pip install wikipedia
import wikipedia
import webbrowser
import os
import smtplib


#initializing engine
engine=pyttsx3.init('sapi5')
voices =engine.getProperty('voices')

#selecting audio
engine.setProperty('voice', voices[0].id)

#string to speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#function to greet the user
def greetuser():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am ROBO Sir. Please tell me how may I help you") 

#function to take audio signal and convert it to string
def takeQuery():
    machine= sr.Recognizer()                         #recognizer initiation
    with sr.Microphone() as audiosource:             #selecting source of input
        print("Listening to you.....")
        machine.pause_threshold=1                     #time gap to accept query
        machine.energy_threshold=400
        audio=machine.listen(audiosource)
    try:
        print("Recognizing") 
        command=machine.recognize_google(audio,language='eng-in') #generating command for user's vocal query
        print(f"Users said: {command}\n")                           #printing user's query
    except Exception as e:
        print("cant recognize say that again please")
        return "None"
    return command                                              #returning input string of vocal query


  
#dictionary holding emailholder's name and their address
dict={'idname1':'address1','idname2':'address2','idname3':'address3','idname4':'address4'}

#function to connect to user's gmail server and sending content to -'to' with body-'content' 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('gmailofuser', 'password')
    server.sendmail('gmaiofuser', to, content)
    server.close()


if  __name__ == "__main__":
   
    greetuser()


    #endlessloop for waititng and recogninzing query
    while True:
        query=takeQuery().lower()

        if 'wikipedia' in query:                                         #handling queries for  wikipedia related queries
            speak("Searching wikipedia")
            query=query.replace("wikipedia","")
            outputs= wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(outputs)
            speak(outputs)

        elif 'open youtube' in query :                                   #handling queries for opening youtube                    
            speak("working on it Sir")
            webbrowser.open("youtube.com")

        elif 'open stackoverflow' in query :                             #handling queries for stackoverflow
            speak("working on it Sir")
            webbrowser.open("stakoverflow.com")

        elif 'open google' in query :                                   #handling queries for opening google chrome browser
            speak("working on it Sir")
            webbrowser.open("google.com")


        elif 'play music' in query:                                     #handling queries for playing music from desired directory
            music_dir = "C:\\Users\\This PC\\Music\\jarvistrack"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:                                       #displaying current time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")


        elif 'open code' in query:                                       #handling queries for opening IDE to run code                           
            codePath = "C:\\Users\\This PC\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


        elif 'email' in query:                                            #handling queries to send email to different contacts  
            try:
                speak("send to who??")                                      #asking for recepient's name
                recipientid=takeQuery().lower()
                speak("What should I say?")                                 #asking for the body of mail
                content = takeQuery()
                to = dict[recipientid]                                      #extracting mail address from recepient's name using global dict
                print(to)   
                sendEmail(to, content)                                      #calling function to connect to server                            
                speak("Email has been sent!")                               
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email") 

        elif 'leave' in query:
            speak("have a good day! sir")                                               #call to exit           
            exit()
        elif 'hello' in query:
            speak("Hii Sir, I hope you are having a great day")