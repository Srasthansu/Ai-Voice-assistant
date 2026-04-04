import os
import eel

from engine.features import *
from engine.command import *

eel.init('www')

playAssistantSound()

os.system('start chrome.exe --app="http://localhost:8000/index.html"')


#eel.browsers.set_path(
    #"chrome",
    #r"C:\Program Files\Google\Chrome\Application\chrome.exe"
#)

eel.start('index.html', mode=None, host='localhost', block=True)