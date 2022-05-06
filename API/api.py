from geopatterns import GeoPattern

import random, string

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

string_to_generate = randomword(10)
pattern = GeoPattern(string_to_generate, generator='xes')
print(pattern.svg_string)
textfile = open("patterntest_%s .svg"%string_to_generate, "w")
a = textfile.write(pattern.svg_string)
textfile.close()