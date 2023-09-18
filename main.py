from viterabot.viterabot import ViteraBot
from viterabot.stray.stray import Stray
from viterabot.observer.subject import Subject


CONFIG = "src\\config.json"
FOLDERS = [
    "src\\database\\image",
    "src\\database\\repository",
    "src\\database\\template"
]
subjectDone = Subject()
subjectStray = Subject()
stray = Stray(subjectStray)
v = ViteraBot(subjectDone=subjectDone, subjectStray=subjectStray,
              config=CONFIG, folders=FOLDERS, stray=stray)
v.run()
