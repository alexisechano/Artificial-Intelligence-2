#Image fun

from PIL import Image

import urllib.request
import io

URL = 'http://www.w3schools.com/css/trolltunga.jpg'
f = io.BytesIO(urllib.request.urlopen(URL).read())

img = Image.open(f)
img.show()
print(img.size)

pix = img.load()
print(pix[2,5])