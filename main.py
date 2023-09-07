import threading
from viterabot.viterabot import ViteraBot
from viterabot.observer.subject import Subject



CONFIG = "config.json"
subjectDone = Subject()
eventRegister = threading.Event()
v = ViteraBot(subjectDone=subjectDone, eventRegister=eventRegister, config=CONFIG)
v.run()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Recebido sinal de interrupção. Parando o programa no proximo clico...")
    v.done()