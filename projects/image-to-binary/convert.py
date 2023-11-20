#   first replace the py.webp file with the img
#   that you want, then replace line 8 with the
#   name you have chosen for the file. now type
#   this:python3 convert.py > output.txt
#   check output.txt for your img conversion
#   it might add a whole new output.txt file btw

from PIL import Image
im = Image.open('py.webp')
pixels = list(im.getdata())
print(pixels)

