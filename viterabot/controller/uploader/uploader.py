import time
from viterabot.controller.uploader.graph.graph import Graph
from viterabot.dao.daoConfig import DaoConfig

class Uploader:
    def __init__(self, graph: Graph, daoConfig: DaoConfig) -> None:
        self.daoConfig = daoConfig
        self.graph = graph

    def sendNextImage(self) -> None:
        ""
        # pegar filename via daoImage.py
        # send next image via self.graph.uploadImage(message, filename)
    
    def done(self) -> None:
        ""