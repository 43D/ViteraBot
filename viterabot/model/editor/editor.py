import time
from viterabot.observer.iObserverAction import iObserverAction

class Editor(iObserverAction):
    def __init__(self, ) -> None:
        self.runnig = True

    def run(self) -> None:
        while(self.runnig):
            # executa verificador na controll, ele verifica se as condições de criar
            # e só para quando for false ele para

            # as condições é, caso 2 ou 3 imagem prontas não enviada ou menos,
            # crie mais umas 5 imagens com textos, as novas imagens devem ser unicas,
            # ou seja, não possuir a mesma combinação já existente

            #esse sleep vai definir de quanto em quanto o verificador será usado
            time.sleep(1)

    def doAction(self, message: str) -> None:
        if message=="done":
            self.done()

    def done(self) -> None:
        self.runnig = False