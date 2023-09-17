import threading
from viterabot.model.editor.editor import Editor
from viterabot.stray.stray import Stray
from viterabot.controller.uploaderManager import UploaderManager
from viterabot.model.uploader.webhook.discord import Discord
from viterabot.model.uploader.graph.graph import Graph
from viterabot.model.uploader.webhook.discord import Discord
from viterabot.controller.registerManager import RegisterManager
from viterabot.dao.daoConfig import DaoConfig
from viterabot.observer.observer import Observer
from viterabot.observer.subject import Subject


class ViteraBot:
    def __init__(self, subjectDone: Subject, subjectStray: Subject, stray: Stray, config: str = "config.json") -> None:
        self.config = config
        self.subjectDone = subjectDone
        self.subjectStray = subjectStray
        self.threadPool = []
        self.stray = stray
        
    def _editor(self) -> None:
        editorObject = Editor()
        observerEditor = Observer(editorObject)
        self.subjectDone.attach(observerEditor)
        editorObject.run()
        
    def _uploader(self) -> None:
        daoConfig = DaoConfig(self.config)
        graph = Graph(daoConfig.getConfig())
        discord = Discord(daoConfig.getConfig())
        uploaderObject = UploaderManager(daoConfig, graph, discord)
        observerUp = Observer(uploaderObject)
        self.subjectDone.attach(observerUp)
        uploaderObject.runUploader()

    def _register(self) -> None:
        rm = RegisterManager()
        observerRm = Observer(rm)
        self.subjectDone.attach(observerRm)
        self.subjectStray.attach(observerRm)

    def _startThead(self, target=None, args=()) -> None:
        thread = threading.Thread(target=target, args=args)
        self.threadPool.append(thread)
        thread.start()

    def run(self) -> None:
        self._startThead(target=self._editor)
        self._startThead(target=self._uploader)
        self._startThead(target=self._register)
        self.stray.run(close=self.done)

    def done(self) -> None:
        self.subjectDone.notify("done")
