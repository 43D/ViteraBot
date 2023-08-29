import threading
from editor import editor as ed
from uploader import uploader as up

editorObject = ed.Editor()
uploaderObject = up.Uploader()

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