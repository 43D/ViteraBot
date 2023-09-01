from viteirabot.controller.uploader.graph.graph import Graph
from viteirabot.dao.daoConfig import DaoConfig

class Uploader:
    def __init__(self, graph: Graph, config: str, dao: DaoConfig):
        self.daoConfig = dao(config)
        self.graph = graph(self.daoConfig.getConfig())

    def sendNextImage(self):
        ""
        # pegar filename via daoImage.py
        # send next image via self.graph.uploadImage(message, filename)