from blog import Blog


class TumblrConsoleView:
    @staticmethod
    def get_input():
        # Input handling is isolated from business logic
        blog_name = input("Enter the Tumblr blog name: ").strip()
        start, end = map(int, input("Enter the range (start-end): ").split("-"))
        return blog_name, start, end

    @staticmethod
    def show_blog_info(blog: Blog):
        print("\nBlog Information")
        print("----------------")
        print(f"title: {blog.title}")
        print(f"name: {blog.name}")
        print(f"description: {blog.description}")
        print(f"no of post: {blog.total_posts}\n")

    @staticmethod
    def show_images(images: dict):
        for post_no, urls in images.items():
            print(f"{post_no}.")
            for url in urls:
                print(f"   {url}")
