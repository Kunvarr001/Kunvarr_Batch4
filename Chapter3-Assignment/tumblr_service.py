from tumblr_api_client import TumblrApiClient
from blog import Blog
from photo_post import PhotoPost


class TumblrService:
    def __init__(self, blog_name: str):
        # Service coordinates API data with domain models
        self.client = TumblrApiClient(blog_name)
        self.data = self.client.fetch_photo_posts()
        self.blog = Blog(self.data)
        self.posts = self.data.get("posts", [])

    def images_in_range(self, start: int, end: int) -> dict:
        images = {}

        for index in range(start - 1, min(end, len(self.posts))):
            post = PhotoPost(self.posts[index])
            images[index + 1] = post.high_resolution_images()

        return images
