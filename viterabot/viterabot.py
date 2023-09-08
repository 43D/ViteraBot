import keyboard
import os
import threading
from viterabot.controller.display import Display
from viterabot.controller.editor.editor import Editor
from viterabot.controller.uploaderManager import UploaderManager
from viterabot.controller.uploader.webhook.discord import Discord
from viterabot.controller.uploader.graph.graph import Graph
from viterabot.controller.uploader.webhook.discord import Discord
from viterabot.controller.registerManager import RegisterManager
from viterabot.dao.daoConfig import DaoConfig
from viterabot.observer.observer import Observer
from viterabot.observer.subject import Subject


class ViteraBot:
    def __init__(self, subjectDone: Subject, eventRegister: threading.Event, display: Display, config: str = "config.json") -> None:
        self.config = config
        self.subjectDone = subjectDone
        self.eventRegister = eventRegister
        self.threadPool = []
        self.display = display

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
        rm = RegisterManager(self.eventRegister)
        observerRm = Observer(rm)
        self.subjectDone.attach(observerRm)
        rm.runRegister()
    
    def _keyboardSetup(self):
        keyboard.on_press_key("p", lambda _:self.eventRegister.set())

    def _startThead(self, target=None, args=()) -> None:
        thread = threading.Thread(target=target, args=args)
        self.threadPool.append(thread)
        thread.start()

    def run(self) -> None:
        self._startThead(target=self._editor)
        self._startThead(target=self._uploader)
        self._startThead(target=self._register)
        self._keyboardSetup()
        self.display.printStart()

    def done(self) -> None:
        self.subjectDone.notify("done")
        self.eventRegister.set()

