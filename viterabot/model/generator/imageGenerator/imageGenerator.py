from viterabot.entity.template import Template
from viterabot.entity.coordinates import Coordinates
from viterabot.entity.mask import Mask
from viterabot.entity.repository import Repository


class ImageGenerator:
    def __init__(self) -> None:
        pass
        
    def generate(self) -> dict:
        return {
            "template": Template(id=0, src_path="logo.png"),
            "imageLuck": [{
                "coordinates": Coordinates(id=0, x_start=100, y_start=100, x_size=200, y_size=200,rotation=45),
                "repository": Repository(id=0, src_path="teste.png", title="vitera")
            }],
            "mask": [{
                "coordinates": Mask(id=0, src_path="teste.png", x_start=300, y_start=20, x_size=250, y_size=250, rotation=0)
            }],
            "hashImage": "5464"
        }
