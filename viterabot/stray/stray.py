import os
import subprocess
import pystray
from PIL import Image
from viterabot.observer.subject import Subject

class Stray:
    def __init__(self, subject: Subject, logado: bool = False) -> None:
        self.logado = logado
        self.subject = subject
        self._create_menu()
        self._create_tray_icon()
        self.close = None

    def _close(self) -> None:
        self.icon.stop()
        if self.close:
            self.close()
        

    def _create_menu(self) -> None:
        self.menu = pystray.Menu(
            pystray.MenuItem('Abrir explorador de arquivo', self._openFileExplorer, default=True),
            pystray.MenuItem('Gerar arquivo de config.', pystray.Menu(
                pystray.MenuItem('GERAR __IMAGEM.json', self.subject.notify("")),
                pystray.MenuItem('GERAR __TEMPLATE.json', self.subject.notify("")),
                pystray.MenuItem('GERAR __MASK.json', self.subject.notify(""))
            )),
            pystray.MenuItem('Registar', pystray.Menu(
                pystray.MenuItem('REGISTRAR TEMPLATES', self.subject.notify("")),
                pystray.MenuItem('REGISTRAR IMAGENS', self.subject.notify("")),
                pystray.MenuItem('REGISTRAR MASCARA', self.subject.notify(""))
            )),
            pystray.MenuItem(lambda text: f'Logado: {self.logado}', self._update),
            pystray.MenuItem('Fechar ViteraBot', self._close)
        )
    def _openFileExplorer(self) -> None:
        projeto_principal = os.getcwd()
        if os.name == 'nt':
            subprocess.Popen(['explorer', projeto_principal])
        elif os.name == 'posix':
            subprocess.Popen(['xdg-open', projeto_principal])

    def _update(self) -> None:
        self.logado = True
        self.icon.update_menu()

    def _create_tray_icon(self) -> None:
        image = Image.open("src\\logo.png")
        self.icon = pystray.Icon("name", image, menu=self.menu)
    
    def run(self, close: object = None) -> None:
        if close:
            self.close = close
        self.icon.run()