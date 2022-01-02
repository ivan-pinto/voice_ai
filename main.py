import speech_recognition as sr
import pyttsx3
import voice

#Voice definition and properties
engine = pyttsx3.init()
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)



#Voice assistant creation
daisy=voice.Assistant()

#Control
execute_daisy = False

#Speak function
def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.

#Listen function
def takecommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=6)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    while True:
        print("Say Hey Daisy to start")
        query = takecommand().lower()
        execute_daisy=daisy.wake(query)
        if execute_daisy == True:
            speak(daisy.wish_me())
        while execute_daisy:
            
            query = takecommand().lower()

            #Browser related options
            if 'wikipedia' in query:
                speak("searching wikipedia")
                talk = daisy.search_wikipedia(query)
                speak(talk)
            
            if 'open youtube' in query:
                daisy.open_youtube()
            
            if 'open google' in query:
                daisy.open_google()

            #Date related options
            if 'the date' in query:
                talk = daisy.tell_me_date()
                speak(talk)
            
            if 'the time' in query:
                talk = daisy.tell_me_time()
                speak(talk)

            #STM control related options

            if 'daisy gateway' in query:
                talk = daisy.stm_command(query)
                speak(talk)
            
            #Fun stuff
            if 'joke' in query:
                talk=daisy.tell_joke()
                speak(talk)

            if 'i am beautiful' in query:
                speak("prettier than you, just me")
            
            if 'first the chicken or the egg' in query:
                speak("chicken, egg, chicken, egg, chicken, egg, chicken, egg. Oops. Stack overflow")

            #Weather
            if 'weather' in query:
                talk = daisy.weather(query)
                speak(talk)

            #Song
            if 'play a song' in query:
                daisy.play_song_pc()

            #Calculator
            if 'calculate' in query:
                talk = daisy.calc(query)
                speak(talk)

            #Sleep
            if 'sleep daisy' in query or 'goodbye daisy' in query:
                execute_daisy = daisy.sleep()
                speak("Goodbye")




