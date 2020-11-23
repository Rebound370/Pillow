#Colton Swartwoudt
#Drawing implementation
#The purpose of this exercise was to
#learn how to use Pillow's ImageDraw module
#in a simple and easy way

import PIL
from PIL import Image, ImageDraw

#Draws a line over the image

def main():
    mech = Image.open("Mech.png")
    drawMech = ImageDraw.Draw(mech)
    drawMech.line((60, 60) + (120, 120), fill = (0, 0, 0), width = 9)
    mech.show()

#Very small and simple program.
#Initally I was confused by the first parameter, the coordinates.
#However after some experimentation, I was able to figure out how
#it worked. I think that the format is pretty strange, but it's
#useable, so I can't complain too much.

if __name__ == "__main__":
    main()