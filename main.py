import threading
from viterabot.controller.editor.editor import Editor
from viterabot.controller.uploaderManager import UploaderManager
from viterabot.controller.uploader.webhook.discord import Discord
from viterabot.controller.uploader.graph.graph import Graph
from viterabot.controller.uploader.webhook.discord import Discord
from viterabot.dao.daoConfig import DaoConfig
from viterabot.observer.observer import Observer
from viterabot.observer.subject import Subject


CONFIG = "config.json"
subject = Subject()

def editor():
    editorObject = Editor()
    observerEditor = Observer(editorObject)
    subject.attach(observerEditor)
    editorObject.run()
    
def uploader():
    daoConfig = DaoConfig(CONFIG)
    graph = Graph(daoConfig.getConfig())
    discord = Discord(daoConfig.getConfig())
    uploaderObject = UploaderManager(daoConfig, graph, discord)
    observerUp = Observer(uploaderObject)
    subject.attach(observerUp)
    uploaderObject.runUploader()

thread1 = threading.Thread(target=editor, args=())
thread2 = threading.Thread(target=uploader, args=())

thread1.start()
thread2.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Recebido sinal de interrupção. Parando o programa no proximo clico...")
    subject.notify("done")

thread1.join()
thread2.join()