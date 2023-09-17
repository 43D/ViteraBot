import threading
from viterabot.viterabot import ViteraBot
from viterabot.stray.stray import Stray
from viterabot.observer.subject import Subject


CONFIG = "config.json"
subjectDone = Subject()
subjectStray = Subject()
eventRegister = threading.Event()
stray = Stray(subjectStray)
v = ViteraBot(subjectDone=subjectDone,subjectStray=subjectStray, eventRegister=eventRegister, config=CONFIG, stray=stray)
v.run()