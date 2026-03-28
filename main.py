import eel

eel.init('www')

eel.browsers.set_path(
    "chrome",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe"
)

eel.start('index.html', mode='chrome-app', size=(1000, 700))