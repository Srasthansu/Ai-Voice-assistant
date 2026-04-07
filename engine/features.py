import re

import pygame
import eel
import os
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import webbrowser
import sqlite3

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
    
    
def extract_yt_term(command):
    
    # Define a regular expession pattern to capture a song name
    
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    
    # Use re.search to find the match in the command
    
    match = re.search(pattern, command, re.IGNORECASE)
    
    # if the match is found return the extracte song name; otherwise return none
    
    return match.group(1) if match else None