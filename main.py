import threading
from viteirabot.controller.editor import editor as ed
from viteirabot.controller.uploader import uploaderManager as up

CONFIG = "config.json"
editorObject = ed.Editor()
uploaderObject = up.UploaderManager(CONFIG)

def editor():
    editorObject.run()

def uploader():
    uploaderObject.run()

thread1 = threading.Thread(target=editor, args=())
thread2 = threading.Thread(target=uploader, args=())

thread1.start()
thread2.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Recebido sinal de interrupção. Parando o programa no proximo clico...")
    editorObject.done()
    uploaderObject.done()

thread1.join()
thread2.join()