from PIL import Image

class ImageEditor:
    def __init__(self) -> None:
        pass

    def edit(self, date: dict) -> None:
        pass



    def _test(self):
        # Abra a imagem principal em que você deseja colocar a outra imagem
        imagem_principal = Image.open("imagem_principal.jpg")

        # Abra a imagem que você deseja colocar por cima da imagem principal
        imagem_overlay = Image.open("imagem_overlay.png")

        # Verifique o tamanho da imagem principal
        largura_principal, altura_principal = imagem_principal.size

        # Redimensione a imagem overlay para que ela tenha o mesmo tamanho da imagem principal
        imagem_overlay = imagem_overlay.resize((largura_principal, altura_principal))

        # Coloque a imagem overlay na imagem principal
        imagem_final = Image.alpha_composite(imagem_principal.convert("RGBA"), imagem_overlay.convert("RGBA"))

        # Salve a imagem final
        imagem_final.save("imagem_final.png")

        # Feche as imagens
        imagem_principal.close()
        imagem_overlay.close()