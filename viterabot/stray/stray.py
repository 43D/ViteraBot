import base64
import io
import os
import subprocess
import pystray
from PIL import Image
from viterabot.observer.subject import Subject

class Stray:
    def __init__(self, subject: Subject, logado: bool = False) -> None:
        self.logado = logado
        self.subject = subject
        self.logo = "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"
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
        msg = base64.b64decode(self.logo)
        buf = io.BytesIO(msg)
        image = Image.open(buf)
        self.icon = pystray.Icon("name", image, menu=self.menu)
    
    def run(self, close: object = None) -> None:
        if close:
            self.close = close
        self.icon.run()