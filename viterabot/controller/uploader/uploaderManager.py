from viterabot.controller.uploader.iUploader import iUploader
from viterabot.dao.daoConfig import DaoConfig

class UploaderManager():
    def __init__(self, dao: DaoConfig, graph: iUploader, discord: iUploader) -> None:
        self.daoConfig = dao
        self.graph = graph
        self.discord = discord

    def _getNextPost(self) -> None:
        ""
        # pegar filename via daoImage.py

    def _sendNextImage(self, message: str, filename: str) -> None:
        self.graph.uploadImage(message, filename)
        self.discord.uploadImage(message, filename)

    def runUploader(self) -> None:
        self._getNextPost()

    def done(self) -> None:
        ""