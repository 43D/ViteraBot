import time
from viteirabot.controller.uploader.graph.graph import Graph
from viteirabot.dao.daoConfig import DaoConfig

class Uploader:
    def __init__(self, graph: Graph, daoConfig: DaoConfig):
        self.daoConfig = daoConfig
        self.graph = graph

    def sendNextImage(self):
        ""
        # pegar filename via daoImage.py
        # send next image via self.graph.uploadImage(message, filename)
    
    def done(self):
        ""