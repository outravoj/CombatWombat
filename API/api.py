from geopatterns import GeoPattern
pattern = GeoPattern('A string for your consideration.', generator='xes')
print(pattern.svg_string)
textfile = open("patterntest.svg", "w")
a = textfile.write(pattern.svg_string)
textfile.close()