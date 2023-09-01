from viterabot.dao.daoMaster import DaoMaster
from viterabot.entity.template import Template

class DaoTemplate:
    def __init__(self, dao: DaoMaster) -> None:
        self.dao = dao
        self.cursor = self.dao.getCursor()

    def func_example_save(self, t: Template) -> None:
        print("teste save template")
        print(t)

    def close(self) -> None:
        self.dao.close()
