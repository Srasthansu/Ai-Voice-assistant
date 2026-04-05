import re

import pygame
import eel
import os
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit

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
    
    if query!="":
        speak("Opening "+query)
        os.system('start '+query)
    else:
        speak("Not Found")
        
        
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