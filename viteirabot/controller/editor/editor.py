import time
from viteirabot.entity.template import Template
from viteirabot.dao.daoMaster import DaoMaster
from viteirabot.dao.model.modelTemplate import DaoTemplate

class Editor():
    def __init__(self, ) -> None:
        self.runnig = True

        #exemplo de injeção indem cagada em python
        path_image = "caminho/para/imagem.jpg"
        title = "tile www"

        template = Template(0, path_image, title)
        dao = DaoMaster()
        daoTemplate = DaoTemplate(dao)
        daoTemplate.func_example_save(template)

    def run(self) -> None:
        while(self.runnig):
            # executa verificador na controll, ele verifica se as condições de criar
            # e só para quando for false ele para

            # as condições é, caso 2 ou 3 imagem prontas não enviada ou menos,
            # crie mais umas 5 imagens com textos, as novas imagens devem ser unicas,
            # ou seja, não possuir a mesma combinação já existente

            #esse sleep vai definir de quanto em quanto o verificador será usado
            time.sleep(1)

    def done(self) -> None:
        self.runnig = False