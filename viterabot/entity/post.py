class Post:
    def __init__(self, id: int, id_image: int, id_facebook: int, discord: bool, published: bool) -> None:
        self.id = id
        self.id_image = id_image
        self.id_facebook = id_facebook
        self.discord = discord
        self.published = published

    def __str__(self) -> None:
        return f"ID: {self.id}\nPath da Imagem: {self.id_image}\nid_facebooko: {self.id_facebook}\ndiscord: {self.discord}\npublished: {self.published}"
