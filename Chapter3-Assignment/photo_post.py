class PhotoPost:
    def __init__(self, post_data: dict):
        # Photos may be absent, so a safe default is required
        self.photos = post_data.get("photos", [])

    def high_resolution_images(self) -> list:
        return [photo.get("photo-url-1280") for photo in self.photos]
