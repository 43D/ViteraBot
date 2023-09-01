import dao

class DaoEditor(dao.Dao):
    def __init__(self):
        super().__init__()
        self.conn = super().getConn()
        self.cursor = self.conn.cursor()

    def getConn(self):
        return self.conn
    
    def getCursor(self):
        return self.cursor
    
    def close(self):
        self.cursor.close()
        self.conn.close()
        