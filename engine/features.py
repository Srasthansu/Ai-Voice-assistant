from playsound import playsound 

import eel

#Playing assistant sound function

@eel.expose
def playAssistantSound():
    music_dir=r"C:\Users\Srasthansu\OneDrive\Desktop\Project\www\assets\audio\start_sound.mp3"
    playsound(music_dir)