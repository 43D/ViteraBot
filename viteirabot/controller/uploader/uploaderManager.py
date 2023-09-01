from viteirabot.controller.uploader.uploader import Uploader
from viteirabot.controller.uploader.graph.graph import Graph
from viteirabot.dao.daoConfig import DaoConfig

class UploaderManager():
    def __init__(self, config: str):
        daoConfig = DaoConfig(config)
        graph = Graph(daoConfig.getConfig())
        self.uploader = Uploader(graph, daoConfig)

    def run(self):
        self.uploader.sendNextImage()

    def done(self):
        self.uploader.done()