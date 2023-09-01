from viterabot.controller.uploader.uploader import Uploader
from viterabot.controller.uploader.graph.graph import Graph
from viterabot.dao.daoConfig import DaoConfig

class UploaderManager():
    def __init__(self, config: str) -> None:
        daoConfig = DaoConfig(config)
        graph = Graph(daoConfig.getConfig())
        self.uploader = Uploader(graph, daoConfig)

    def run(self) -> None:
        self.uploader.sendNextImage()

    def done(self) -> None:
        self.uploader.done()