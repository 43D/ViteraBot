from viterabot.viterabot import ViteraBot
from viterabot.stray.stray import Stray
from viterabot.observer.subject import Subject


CONFIG = "config.json"
subjectDone = Subject()
subjectStray = Subject()
stray = Stray(subjectStray)
v = ViteraBot(subjectDone=subjectDone,subjectStray=subjectStray, config=CONFIG, stray=stray)
v.run()