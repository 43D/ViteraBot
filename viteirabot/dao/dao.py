import sqlite3
import os
import json

class Dao:
    def __init__(self):
        self.db = "viteiraBot.db"
        sqlite3.connect(self.db)
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
    
    def getConfig(self, config):
        try:
            with open(config, 'r') as arquivo:
                data_dict = json.load(arquivo)
            return data_dict
        except FileNotFoundError:
            print(f"O arquivo '{config}' não foi encontrado.")
            return None
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON no arquivo '{config}': {e}")
            return None

    def getConn(self):
        return sqlite3.connect(self.db)