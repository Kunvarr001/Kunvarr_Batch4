from tumblr_service import TumblrService
from tumblr_console_view import TumblrConsoleView


class TumblrApplication:
    @staticmethod
    def run():
        try:
            # Entry point delegates work instead of implementing logic
            blog_name, start, end = TumblrConsoleView.get_input()
            print("\nFetching data, please wait...\n")

            service = TumblrService(blog_name)

            TumblrConsoleView.show_blog_info(service.blog)
            images = service.images_in_range(start, end)
            TumblrConsoleView.show_images(images)

        except Exception as error:
            print("Error:", error)


if __name__ == "__main__":
    TumblrApplication.run()
