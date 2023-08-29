class Image:

    def __init__(self, id, path_image, tags, title):
        self.id = id
        self.path_image = path_image
        self.tags = tags
        self.title = title

    def __str__(self):
        return f"Título: {self.title}\nPath da Imagem: {self.path_image}\nTags: {self.tags}"