import time
from viterabot.model.editor.iEditor import iEditor
from viterabot.model.generator.iGenerator import iGenerator
from viterabot.observer.iObserverAction import iObserverAction

class GeneratorManager(iObserverAction):
    def __init__(self, editor: iEditor, imageGenerator: iGenerator) -> None:
        self.running = True
        self.editor = editor
        self.imageGenerator = imageGenerator
        self._resetCount()
        
    def _resetCount(self):
        self.count = 60*60

    def run(self):
        while self.running:
            time.sleep(1)
            self.count-=1
            if(self.count<=0):
                # execute
                self._resetCount()


    def doAction(self, message: str) -> None:
        if message=="done":
            self.done()

    def done(self) -> None:
        self.running = False