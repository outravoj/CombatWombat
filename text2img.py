from PIL import Image, ImageFont, ImageDraw
import random
import numpy as np


def place_text(image: Image, text: str) -> Image:
    RGB = np.array([255, 255, 255])
    my_array = np.asarray(image)
    title_font = ImageFont.truetype('Montserrat-Black.ttf', 20)
    text_size = title_font.getsize(text)
    image_editable = ImageDraw.Draw(image)
    randomized_coords = (random.randint(0, my_array.shape[1] - text_size[0]), random.randint(0, my_array.shape[0] - text_size[1]))
    print("the tuple is: ", randomized_coords)
    color_rgb = tuple(RGB - np.floor(np.mean(my_array[randomized_coords[1]:randomized_coords[1]+text_size[1], randomized_coords[0]:randomized_coords[0]+text_size[0], :], axis=(0,1))).astype(int))
    image_editable.text(randomized_coords, text, color_rgb, font=title_font)

    return image
