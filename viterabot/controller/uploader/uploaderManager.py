from viterabot.controller.uploader.webhook.discord import Discord
from viterabot.controller.uploader.graph.graph import Graph
from viterabot.dao.daoConfig import DaoConfig

class UploaderManager():
    def __init__(self, config: str) -> None:
        self.daoConfig = DaoConfig(config)
        self.graph = Graph(self.daoConfig.getConfig())
        self.discord = Discord(self.daoConfig.getConfig())

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