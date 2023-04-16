from PIL import Image

"""
Constants for the image
"""

IMAGE_WIDTH = 420
IMAGE_HEIGHT = 300
IMAGE_LOAD_TIME = 100

"""
Adds the image
"""

MY_FILE = "/Users/pkumar030c/Downloads/Euler.jpeg"
image = Image.open(MY_FILE)
image = image.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
image.save("new.png")

"""
Modifies each color channel in a pixel depending on its value
to either 25 more or 25 less than its original value
"""


def custom_filter(pixel):
    new_pixel = []
    for item in pixel:
        if item > 127:
            new_pixel.append(min(item + 25, 255))
        else:
            new_pixel.append(max(item - 25, 0))
    return tuple(new_pixel)


"""
Sets every pixel in an image to the modified one from the
custom_filter function
"""


def change_image():
    for x in range(IMAGE_WIDTH):
        for y in range(IMAGE_HEIGHT):
            xy = (x, y)
            pixel = image.getpixel(xy)
            change = custom_filter(pixel)
            image.putpixel(xy, change)

    image.show()


change_image()
