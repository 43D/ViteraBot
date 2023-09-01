import time
from viteirabot.controller.uploader.uploader import Uploader
from viteirabot.controller.uploader.graph.graph import Graph
from viteirabot.dao.daoConfig import DaoConfig

class UploaderManager():
    def __init__(self, config: str):
        self.runnig = True
        self.config = config
        self.uploader = Uploader(Graph, self.config, DaoConfig)

    def run(self):
        while(self.runnig):
            self.uploader.sendNextImage()
            time.sleep(3*60*60)
            
    def done(self):
        self.runnig = False