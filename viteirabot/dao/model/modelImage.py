from viteirabot.dao.daoMaster import DaoMaster
from viteirabot.entity.image import Image

class DaoImage:
    def __init__(self, dao: DaoMaster) -> None:
        self.dao = dao
        self.cursor = self.dao.getCursor()

    def func_example_save(self, t: Image) -> None:
        print("teste save Image")
        print(t)

    def close(self) -> None:
        self.dao.close()
