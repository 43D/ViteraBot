import time
from viterabot.model.uploader.iUploader import iUploader
from viterabot.dao.daoFiles import DaoFiles
from viterabot.observer.iObserverAction import iObserverAction

class UploaderManager(iObserverAction):
    def __init__(self, dao: DaoFiles, graph: iUploader, discord: iUploader) -> None:
        self.running = True
        self.daoFiles = dao
        self.graph = graph
        self.discord = discord
        self._resetCount()

    def _resetCount(self) -> None:
        self.count = 60*60

    def _getNextPost(self) -> None:
        ""
        # pegar filename via daoImage.py

    def _sendNextImage(self, message: str, filename: str) -> None:
        self.graph.uploadImage(message, filename)
        self.discord.uploadImage(message, filename)

    def run(self) -> None:
        while self.running:
            time.sleep(1)
            self.count-=1
            if(self.count<=0):
                # execute
                self._getNextPost()
                self._resetCount()

    def doAction(self, message: str) -> None:
        if message=="done":
            self.done()

    def done(self) -> None:
        self.running = False