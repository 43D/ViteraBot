class Template:
    def __init__(self, id: int, src_path: str, title: str) -> None:
        self.id = id
        self.src_path = src_path
        self.title = title

    def __str__(self) -> None:
        return f"Path da Imagem: {self.src_path}\ntitle: {self.title}"