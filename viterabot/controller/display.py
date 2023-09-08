import os

class Display:
    def __init__(self) -> None:
        self.autenticado = False

    
    def _clearConsole(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def printStart(self):
        self._clearConsole()
        print("Aperte as teclas para algo...")
        print("A - GERAR __IMAGEM.json")
        print("S - GERAR __TEMPLATE.json")
        print("D - GERAR __MASK.json")
        print("Z - REGISTRAR TEMPLATES")
        print("X - REGISTRAR IMAGENS")
        print("C - REGISTRAR MASCARA")
        print("")
        if self.autenticado:
            print("Status: logado")
        else:
            print("L - Para fazer login")

        print("Ctrl + C para sair")