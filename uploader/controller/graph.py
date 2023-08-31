from pyfacebook import GraphAPI

class Graph:
    def __init__(self, config: dict):
        self.app_id = config["app_id"]
        self.app_secret = config["app_secret"]
        self.access_token = config["access_token"]
        self.api = GraphAPI(
            app_id=self.app_id,
            app_secret=self.app_secret,
            access_token=self.access_token
        )
        print(self.api)

    def uploadImage(self, message, filename):
        self.api.post_object(object_id="me", connection="photos",
                data={"message": message, "published": True},
                files={"image": (filename, open(filename,'rb'), 'image/png')}
        )
        print(f"File ${filename} is uploaded")