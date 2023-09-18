from PIL import Image
from viterabot.entity.image import Image as im

class ImageEditor:
    def __init__(self) -> None:
        self.pool = []

    def _setTemplate(self, file) -> None:
        self.template = Image.open(file)
        self.template = self.template.convert("RGBA")

    def _editOverlay(self, data)-> None:
        for image in data:
            overlay = Image.open(image["repository"].src_path)
            overlay = overlay.convert("RGBA")
            overlay = overlay.resize((image["coordinates"].x_size, image["coordinates"].y_size))
            overlay = overlay.rotate(image["coordinates"].rotation, expand=True)
            self.template.alpha_composite(overlay, (image["coordinates"].x_start, image["coordinates"].y_start))
            self.pool.append(overlay)

    def _editMAsk(self, data)-> None:
        for image in data:
            mask = Image.open(image["coordinates"].src_path)
            mask = mask.convert("RGBA")
            mask = mask.resize((image["coordinates"].x_size, image["coordinates"].y_size))
            mask= mask.rotate(image["coordinates"].rotation, expand=True)
            self.template.alpha_composite(mask, (image["coordinates"].x_start, image["coordinates"].y_start))
            self.pool.append(mask)
        
    def _save(self, path: str):
        self.template.save(path)

    def edit(self, data: dict) -> im:
        self._setTemplate(data["template"].src_path)
        self._editOverlay(data["imageLuck"])
        self._editMAsk(data["mask"])
        self.pool.append(self.template)
        img = im(src_path="imagem_final.png", hashImage=data["hashImage"], title="", id=0)
        self._save(img.src_path)
        self._done()
        return img

    def _done(self):
        for i in self.pool:
            i.close()
