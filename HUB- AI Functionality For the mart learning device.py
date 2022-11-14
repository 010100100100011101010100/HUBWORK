#importing all the important modules 
import pyttsx3
import datetime

# defining the microsoft API for speech recognition
engine = pyttsx3.init('sapi5')

#getting details of current voice
voices= engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

#We define a function speak to convert our text to speech
def speak(audio):
engine.say(audio) 
engine.runAndWait()

#Initiating the intro which the virtual AI will say after being called for
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your virtual study guide. Please tell me how may I help you") 



#We define this function to the user speech input which will be most likely be given by a student 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

 try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:
          
        print("Say that again please...")   
    return query

#functionality to open various sites such as wikipedia,stackoverflowand tell time, which consist of the main learning resources for the student
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower() 

        
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
