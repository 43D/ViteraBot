class Image:

    def __init__(self, id: int, src_path: str, title: str, has: str) -> None:
        self.id = id
        self.src_path = src_path
        self.hash = hash
        self.title = title

    def __str__(self) -> None:
        return f"Título: {self.title}\nPath da Imagem: {self.src_path}\nhash: {self.hash}"