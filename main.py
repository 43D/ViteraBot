import threading
from viterabot.controller.editor.editor import Editor
from viterabot.controller.uploader.uploaderManager import UploaderManager
from viterabot.controller.uploader.webhook.discord import Discord
from viterabot.controller.uploader.graph.graph import Graph
from viterabot.controller.uploader.webhook.discord import Discord
from viterabot.dao.daoConfig import DaoConfig

CONFIG = "config.json"

daoConfig = DaoConfig(CONFIG)
graph = Graph(daoConfig.getConfig())
discord = Discord(daoConfig.getConfig())
uploaderObject = UploaderManager(daoConfig, graph, discord)

editorObject = Editor()

def editor():
    editorObject.run()

def uploader():
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
    editorObject.done()
    uploaderObject.done()

thread1.join()
thread2.join()