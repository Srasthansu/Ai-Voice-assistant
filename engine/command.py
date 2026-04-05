import pyttsx3
import speech_recognition as sr
import eel
import sounddevice as sd
import numpy as np
import time

# -----------------------
# Initialize TTS engine once
# -----------------------
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 174)

def speak(text):
    """Speak the given text using pyttsx3."""
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

# -----------------------
# Voice recognition
# -----------------------

def takecommand():
    r = sr.Recognizer()
    
    fs = 16000      # Sampling rate
    duration = 5    # seconds to record
    print("Listening...")
    eel.DisplayMessage("Listening...")

    # Record audio using sounddevice
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    # Convert to AudioData for speech_recognition
    audio_data = sr.AudioData(recording.tobytes(), fs, 2)  # 16-bit audio
    
    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio_data, language='en-in')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        # Speak the recognized text
        
        
    except Exception as e:
        print("Error:", e)
        return ""
    
    return query.lower()

@eel.expose
def allCommands():
    
    query=takecommand()
    print(query)
    
    if "open" in query:
        from engine.features import openCommand
        openCommand(query)
    
    elif "on youtube":
        from engine.features import PlayYoutube
        PlayYoutube(query)
    
    
    else:
        print("Not run")    
    
    eel.ShowHood()