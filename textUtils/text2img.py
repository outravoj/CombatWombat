from PIL import Image, ImageFont, ImageDraw
import random
import numpy as np

# BASIC COLORS
WHITE = np.array([255, 255, 255])
BLACK = np.array([0, 0, 0])

# FONT SIZE, TEXT OFFSETS FOR WOMBO AND BREAK LENGTH
FONT_SIZE_NAME = 27
FONT_SIZE_TEXT = 60
TL_OFFSET = 45
TT_OFFSET = 35
NAME_OFFSET = 12
BR_OFFSET = 45
BB_OFFSET = 55
BREAK_LENGTH = 20

def get_color(image_array: np.ndarray, text_coords: tuple, text_size: tuple) -> tuple:
    color_mean = np.floor(np.mean(image_array[text_coords[1]:text_coords[1] + text_size[1], text_coords[0]:text_coords[0] + text_size[0], :], axis=(0, 1))).astype(int)
    luminance = (0.299 * color_mean[0] + 0.587 * color_mean[1] + 0.114 * color_mean[2]) / 255
    if luminance > 0.5:
        color_rgb = tuple(BLACK)
    else:
        color_rgb = tuple(WHITE)

    return color_rgb

def preprocess_name(name: str) -> str:
    new_name = ""
    new_name_list = name.split()
    list_length = len(new_name_list)
    for i, item in enumerate(new_name_list):
        new_name += item
        if i + 1 != list_length:
            new_name += " "

    return new_name

def preprocess_text(text: str) -> str:
    new_text = ""
    new_line = ""
    new_text_list = text.split()
    for item in new_text_list:
        if len(new_line) == 0:
            new_line += item
        elif len(new_line) + len(item) + 1 < BREAK_LENGTH:
            new_line += " "
            new_line += item
        else:
            new_line += "\n"
            new_text += new_line
            new_line = item

    new_text += new_line
    return new_text

def place_text(image: Image, name1: str, name2: str, text: str) -> Image:
    name1 = preprocess_name(name1)
    name2 = preprocess_name(name2)
    text = preprocess_text(text)
    strings = [name1, name2, text]
    image_array = np.asarray(image)
    name_font = ImageFont.truetype('fonts/Montserrat-Medium.ttf', FONT_SIZE_NAME)
    text_font = ImageFont.truetype('fonts/Montserrat-Black.ttf', FONT_SIZE_TEXT)
    image_editable = ImageDraw.Draw(image)
    name1_size = None
    name1_coords = None
    name2_size = None
    name2_coords = None

    for i, string in enumerate(strings):
        if i == 0:
            name1_size = name_font.getsize_multiline(string)
            name1_coords = (TL_OFFSET, TT_OFFSET)
            #print(name1_size, name1_coords)
            color_rgb = get_color(image_array, name1_coords, name1_size)
            image_editable.text(name1_coords, string, color_rgb, font=name_font)

        elif i == 1:
            name2_size = name_font.getsize_multiline(string)
            name2_coords = (TL_OFFSET, TT_OFFSET + NAME_OFFSET + name1_size[1])
            #print(name2_size, name2_coords)
            color_rgb = get_color(image_array, name2_coords, name2_size)
            image_editable.text(name2_coords, string, color_rgb, font=name_font)

        elif i == 2:
            text_size = text_font.getsize_multiline(string)
            text_coords = (random.randint(TL_OFFSET, image_array.shape[1] - text_size[0] - BR_OFFSET),
                           random.randint(TT_OFFSET + 2 * NAME_OFFSET + name1_size[1] + name2_size[1], image_array.shape[0] - text_size[1] - BB_OFFSET))
            #print(text_size, text_coords)
            color_rgb = get_color(image_array, text_coords, text_size)
            image_editable.text(text_coords, string, color_rgb, font=text_font)

    # UNCOMMENT FOR DISPLAYING THE IMAGE
    #image.show()

    return image

if __name__ == "__main__":
    place_text(Image.open("wombo.jpg"), "  \t Lukas     Halaska   \n\t", "\n Vojtech  \n \t Outrata  \t", "African bees  \n \t  can\t\t\n   suck\n  \nmassive \n\t cocks.")