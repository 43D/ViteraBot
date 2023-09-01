from pyfacebook import GraphAPI
from viterabot.controller.uploader.iUploader import iUploader

class Graph(iUploader):
    def __init__(self, config: dict) -> None:
        self.app_id = config["app_id"]
        self.app_secret = config["app_secret"]
        self.access_token = config["access_token"]
        self.api = GraphAPI(
            app_id=self.app_id,
            app_secret=self.app_secret,
            access_token=self.access_token
        )

    def uploadImage(self, message: str, filename: str) -> None:
        self.api.post_object(object_id="me", connection="photos",
                data={"message": message, "published": True},
                files={"image": (filename, open(filename,'rb'), 'image/png')}
        )
        print(f"File ${filename} is uploaded")