import json

class DaoConfig:
    def __init__(self, CONFIG: str):
        self.CONFIG = CONFIG

    def getConfig(self):
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