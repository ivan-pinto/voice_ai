import speech_recognition as sr
import pyttsx3
import voice

#Voice definition and properties
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)

#Voice assistant creation
vera=voice.Assistant()

#Speak function
def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.

#Listen function
def takecommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

#Wish me function
def wish_me():
    hour = int(vera.tell_me_hour())
    if hour >= 0 and hour < 12:
        speak("good morning, i am your virtual assistant")
    elif hour >= 12 and hour < 18:
        speak("good afternoon, i am your virtual assistant")
    else:
        speak("hello, i am your virtual assistant")


if __name__ == "__main__":
    wish_me()
    while True:
        query = takecommand().lower()

        #Browser related options
        if 'wikipedia' in query:
            speak("searching wikipedia")
            talk = vera.search_wikipedia(query)
            speak(talk)
        
        if 'open youtube' in query:
            vera.open_youtube()
        
        if 'open google' in query:
            vera.open_google()

        #Date related options
        if 'the date' in query:
            talk = vera.tell_me_date()
            speak(talk)
        
        if 'the time' in query:
            talk = vera.tell_me_time()
            speak(talk)

        #STM control related options

        if 'sd' in query:
            talk = vera.stm_command(query)
            speak(talk)
        
        #Fun stuff
        if 'joke' in query:
            talk=vera.tell_joke()
            speak(talk)



