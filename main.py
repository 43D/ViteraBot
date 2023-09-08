import threading
from viterabot.viterabot import ViteraBot
from viterabot.controller.display import Display
from viterabot.observer.subject import Subject



CONFIG = "config.json"
subjectDone = Subject()
eventRegister = threading.Event()
display = Display()
v = ViteraBot(subjectDone=subjectDone, eventRegister=eventRegister, config=CONFIG, display=display)
v.run()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Recebido sinal de interrupção. Parando o programa no proximo clico...")
    v.done()