import sqlite3

class Dao:
    def __init__(self):
        self.db = "viteiraBot.db"
        sqlite3.connect(self.db)
        self._folder()

    def _folder(self):
        #check folder exits
        #check and save database folders local
        print("teste")
        
    def getConn(self):
        return sqlite3.connect(self.db)