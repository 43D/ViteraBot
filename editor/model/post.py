class Post:
    def __init__(self, id, path_image, text):
        self.id = id
        self.path_image = path_image
        self.text = text

    def __str__(self):
        return f"ID: {self.id}\nPath da Imagem: {self.path_image}\nTexto: {self.text}"
