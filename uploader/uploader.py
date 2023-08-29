import time

class Uploader():
    def __init__(self):
        self.runnig = True

    def run(self):
        while(self.runnig):
            # de tempo em tempo é chamado o enviador na controller
            # ele pega a proxima img, chama o gerador de texto na controller e envia

            # esse sleep define de quanto em quanto a imagem será enviada
            time.sleep(1)
            
    def done(self):
        self.runnig = False