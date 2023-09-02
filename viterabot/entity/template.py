class Template:
    def __init__(self, id: int, src_path: str) -> None:
        self.id = id
        self.src_path = src_path

    def __str__(self) -> None:
        return f"ID: {self.id}\nPath da Imagem: {self.src_path}\n"