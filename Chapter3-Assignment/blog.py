class Blog:
    def __init__(self, data: dict):
        # Blog metadata is grouped into a domain object
        tumblelog = data.get("tumblelog", {})
        self.title = tumblelog.get("title", "")
        self.name = tumblelog.get("name", "")
        self.description = tumblelog.get("description", "")
        self.total_posts = data.get("posts-total", 0)
