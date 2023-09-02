import time
from viterabot.controller.uploader.iUploader import iUploader
from viterabot.dao.daoConfig import DaoConfig
from viterabot.observer.interface_observer_action import ObserverActionInterface

class UploaderManager(ObserverActionInterface):
    def __init__(self, dao: DaoConfig, graph: iUploader, discord: iUploader) -> None:
        self.daoConfig = dao
        self.graph = graph
        self.discord = discord
        self.time = 1

    def _getNextPost(self) -> None:
        ""
        # pegar filename via daoImage.py

    def _sendNextImage(self, message: str, filename: str) -> None:
        self.graph.uploadImage(message, filename)
        self.discord.uploadImage(message, filename)

    def runUploader(self) -> None:
        self.running = True
        while(self.running):
            self._getNextPost()
            time.sleep(self.time)

    def do_action(self, message: str) -> None:
        if message=="done":
            self.done()

    def done(self) -> None:
        self.running = False