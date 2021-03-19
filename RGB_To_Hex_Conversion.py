# https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb(r, g, b):
    r, g, b = 0 if r < 0 else r, 0 if g < 0 else g, 0 if b < 0 else b
    r, g, b = 255 if r > 255 else r, 255 if g > 255 else g, 255 if b > 255 else b
    return "%0.2X" % r + "%0.2X" % g + "%0.2X" % b
