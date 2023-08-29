from editor.dao.daoEditor import DaoEditor
from editor.model.image import Image

class DaoImage:
    def __init__(self, dao: DaoEditor):
        self.dao = dao
        self.cursor = self.dao.getCursor()

    def func_example_save(self, t: Image):
        print("teste save Image")
        print(t)
