import re
import struct
import time

import numpy as np
import pvporcupine
import pygame
import eel
import os
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import webbrowser
import sqlite3
import sounddevice as sd

from engine.helper import extract_yt_term

conn = sqlite3.connect("Luffy.db")
cursor = conn.cursor()

def playAssistantSound():
    pygame.mixer.init()

    pygame.mixer.music.load(
        r"C:\Users\IT Kalyani\OneDrive - PDx Research Labs LLP\Desktop\Project\www\assets\audio\start_sound (1).mp3"
    )

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue
    

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()
    
    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")
        
        
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing"+search_term+"on YouTube")
    kit.playonyt(search_term)
    
    
def hotword():
     
    porcupine = None
    audio_stream = None

    try:
        # pre trained keywords    
        porcupine = pvporcupine.create(keywords=["jarvis", "alexa"]) 

        def callback(indata, frames, time_info, status):
            if status:
                print(status)

            pcm = np.frombuffer(indata, dtype=np.int16)

            for i in range(0, len(pcm), porcupine.frame_length):
                frame = pcm[i:i + porcupine.frame_length]

                if len(frame) == porcupine.frame_length:
                    keyword_index = porcupine.process(frame)

                    if keyword_index >= 0:
                        print("hotword detected")

                        import pyautogui as autogui
                        autogui.keyDown("win")
                        autogui.press("j")
                        time.sleep(2)
                        autogui.keyUp("win")

        with sd.InputStream(
            samplerate=porcupine.sample_rate,
            channels=1,
            dtype='int16',
            blocksize=porcupine.frame_length,
            callback=callback
        ):
            while True:
                time.sleep(0.1)

    except Exception as e:
        print("Error:", e)

    finally:
        if porcupine is not None:
            porcupine.delete()