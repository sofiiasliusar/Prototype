# THIS METHOD IS BETTER - images are perfectly fitting the screen and the code is short

# from kivy.app import App
# from kivy.uix.carousel import Carousel
# from kivy.uix.image import AsyncImage


# class Trial(App):
#     def build(self):
#         carousel = Carousel(direction='right')
#         for i in range(10):
#             src = "http://placehold.it/480x270.png&text=slide-%d&.png" % i
#             image = AsyncImage(source=src, fit_mode="contain")
#             carousel.add_widget(image)
#         return carousel


# Trial().run()
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image
from kivy.core.window import Window

# Set the window size to emulate a common smartphone size (e.g., iPhone 6/7/8)
Window.size = (375, 667)

class ImageCarouselApp(App):
    def build(self):
        carousel = Carousel(direction='right', loop=True)
        # List of image paths
        images = ["4.jpg", "6.jpg", "5.png"]

        # Add images to the Carousel
        for img in images:
            image = Image(source=img, allow_stretch=True, keep_ratio=False)
            carousel.add_widget(image)

        return carousel

# Run the application
if __name__ == '__main__':
    ImageCarouselApp().run()
