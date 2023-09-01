
from discord_webhook import DiscordWebhook, DiscordEmbed
from viterabot.controller.uploader.iUploader import iUploader

class Discord(iUploader):
    def __init__(self, config: dict) -> None:
        self.url = config["discord_webhook"]
        self.webhook = DiscordWebhook(url=self.url, username="ViteraBot",
                                      avatar_url='https://43d.github.io/ViteraBot/logo.png')

    def _send(self) -> None:
        self.webhook.execute()
        print("Discord is uploaded")

    def uploadImage(self, message: str, filename: str) -> None:
        embed = DiscordEmbed(title="ViteraBot 3", description=message, color="03b2f8")

        with open(filename, "rb") as f:
            self.webhook.add_file(file=f.read(), filename="image.png")

        embed.set_image(url="attachment://image.png")
        self.webhook.add_embed(embed)

        self._send()