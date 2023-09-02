class Image:
    def __init__(self, id: int, src_path: str, title: str, hashImage: str) -> None:
        self.id = id
        self.src_path = src_path
        self.title = title
        self.hashImage = hashImage

    def __str__(self) -> None:
        return f"Título: {self.title}\nPath da Imagem: {self.src_path}\nhash: {self.hashImage}"