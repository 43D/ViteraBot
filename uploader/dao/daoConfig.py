import dao

class DaoConfig(dao.Dao):
    def __init__(self, CONFIG: str):
        super().__init__()
        self.CONFIG = CONFIG

    def getConfig(self):
        return super().getConfig(self.CONFIG)
