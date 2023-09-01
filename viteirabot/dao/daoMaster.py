import sqlite3
import os
import json

class DaoMaster:
    def __init__(self):
        self.db = "viteiraBot.db"
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()
        self._folder()
        
    def _checkConfig(self):
        if not os.path.exists('config.json'):
            config_data = {
                "app_id":"",
                "app_secret":"",
                "access_token":"",
                "time_post": 180
            }
            with open('config.json', 'w') as config_file:
                json.dump(config_data, config_file, indent=4)

    def _folder(self):
        self._checkConfig()
        #check folder exits
        #check and save database folders local
        print("teste")

    def getCursor(self):
        return self.cursor
    
    def close(self):
        self.cursor.close()
        self.conn.close()
    
        