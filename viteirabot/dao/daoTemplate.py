from editor.dao.daoEditor import DaoEditor
from editor.model.template import Template

class DaoTemplate:
    def __init__(self, dao: DaoEditor):
        self.dao = dao
        self.cursor = self.dao.getCursor()

    def func_example_save(self, t: Template):
        print("teste save template")
        print(t)
