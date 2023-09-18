import os
import json

class DaoFiles:
    def __init__(self, CONFIG: str, folders: [str]) -> None:
        self.CONFIG = CONFIG
        self.folders = folders
        self._folder()
        
    def _checkConfig(self) -> None:
        if not os.path.exists(self.CONFIG):
            config_data = {
                "app_id":"",
                "app_secret":"",
                "access_token":"",
                "time_post": 180,
                "discord_webhook":""
            }
            with open(self.CONFIG, 'w') as config_file:
                json.dump(config_data, config_file, indent=4)

    def _createFolder(self, folder : str) -> None:
        if not os.path.exists(folder):
            os.makedirs(folder)

    def _folder(self) -> None:
        self._checkConfig()
        for item in self.folders:
            self._createFolder(item)

    def getConfig(self) -> dict:
        try:
            with open(self.CONFIG, 'r') as arquivo:
                data_dict = json.load(arquivo)
            return data_dict
        except FileNotFoundError:
            print(f"O arquivo '{self.CONFIG}' não foi encontrado.")
            return None
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON no arquivo '{self.CONFIG}': {e}")
            return None