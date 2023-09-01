class Post:
    def __init__(self, id: int, id_image: int, id_post: int, published: bool) -> None:
        self.id = id
        self.id_image = id_image
        self.id_post = id_post
        self.published = published

    def __str__(self) -> None:
        return f"ID: {self.id}\nPath da Imagem: {self.id_image}\nid_posto: {self.id_post}\npublished: {self.published}"
