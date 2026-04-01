import eel

from engine.features import *

eel.init('www')

playAssistantSound()

eel.browsers.set_path(
    "chrome",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe"
)

eel.start('index.html', mode='chrome-app', size=(1000, 700))