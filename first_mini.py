#Image fun

from PIL import Image

import urllib.request
import io

def find_third(num):
    if num >= 0 and num < 85:
        return 0
    elif num >= 85 and num < (85*2):
        return 127
    else:
        return 255

URL = 'http://www.w3schools.com/css/trolltunga.jpg'
f = io.BytesIO(urllib.request.urlopen(URL).read())

img = Image.open(f)
#img.show()
print(img.size)

pix = img.load()
print(pix[2,5])


#new part
for x in range(img.size[0]):
    for y in range(img.size[1]):
        current_color = pix[x,y]

        new_color = 0, 0, 0

        red = current_color[0]
        green = current_color[1]
        blue = current_color[2]

        new_color = (find_third(red), find_third(green), find_third(blue))

        pix[x,y] = new_color

img.show()