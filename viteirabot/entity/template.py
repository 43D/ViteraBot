class Template:

    def __init__(self, id, path_image, tags, coordinates_lists):
        self.id = id
        self.path_image = path_image
        self.tags = tags
        self.coordinates_lists = coordinates_lists

    def __str__(self):
        return f"Path da Imagem: {self.path_image}\nTags: {self.tags}\nCoordenadas: {self.coordinates_lists}"