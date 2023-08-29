import time
from editor.model.template import Template
from editor.dao.daoEditor import DaoEditor
from editor.dao.daoTemplate import DaoTemplate

class Editor():
    def __init__(self, ):
        self.runnig = True

        #exemplo de injeção indem cagada em python
        path_image = "caminho/para/imagem.jpg"
        tags = ["tag1", "tag2", "tag3"]
        coordinates_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        template = Template(0, path_image, tags, coordinates_lists)
        dao = DaoEditor()
        daoTemplate = DaoTemplate(dao)
        daoTemplate.func_example_save(template)

    def run(self):
        while(self.runnig):
            # executa verificador na controll, ele verifica se as condições de criar
            # e só para quando for false ele para

            # as condições é, caso 2 ou 3 imagem prontas não enviada ou menos,
            # crie mais umas 5 imagens com textos, as novas imagens devem ser unicas,
            # ou seja, não possuir a mesma combinação já existente

            #esse sleep vai definir de quanto em quanto o verificador será usado
            time.sleep(1)

    def done(self):
        self.runnig = False