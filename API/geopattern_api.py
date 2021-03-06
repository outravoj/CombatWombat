from geopatterns import GeoPattern
import random, string
from PIL import Image
import cairosvg

generators = ['xes', 'squares', 'triangles','hexagons', 'sinewaves', 'plus_signs']

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generatePattern(word_in_sting):
    pattern = GeoPattern(word_in_sting, generator=generators[random.randint(0,(len(generators)-1))])
    cairosvg.svg2png(bytestring=pattern.svg_string, write_to="images/patterntest_%s.png"%word_in_sting)
    fp = open("images/patterntest_%s.png"%word_in_sting, "rb")
    pil_image = Image.open(fp, mode='r', formats=None)
    return pil_image

if __name__ == "__main__":
    string_to_generate = randomword(10)
    pattern = GeoPattern(string_to_generate, generator=generators[random.randint(0,(len(generators)-1))])
    print(pattern.svg_string)
    textfile = open("patterntest_%s.svg"%string_to_generate, "w")
    a = textfile.write(pattern.svg_string)
    textfile.close()

    cairosvg.svg2png(bytestring=pattern.svg_string, write_to="images/patterntest_%s.png"%string_to_generate)

    fp = open("images/patterntest_%s.png"%string_to_generate, "rb")
    pil_image = Image.open(fp, mode='r', formats=None)
    pil_image.show()

    print(len(generators))