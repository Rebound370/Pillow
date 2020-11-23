#Colton Swartwoudt
#Composite Pictures
#The purpose of this exercise was to
#use ImageChops to blend two images

import PIL
from PIL import Image, ImageFilter, ImageChops, ImageDraw

def main():
    print("a")
    mech = Image.open("Mech.png")
    ellipse = Image.open("Ellipse.png")
    ellipse = ellipse.convert("RGB")
    output = ImageChops.blend(mech, ellipse, 0.5)
    output.show()

#Initailly I had difficulty figuring out how to create a secondary picture to composite.
#My initial attempts just led to me drawing over the image.
#Then I decided to create the secondary image externally and apply it here.
#I decided that I would learn how to create images from scratch later.
#Then I ran into a value error stating that the "images do not match",
#despite being the same size. I then discovered that these images needed to
#be the same mode, and despite both being imported the same way,
#Pillow was smart enough to register the black and white image as "L" mode.
#I then had to convert the black and white ellipse to "RGB" mode, and it
#worked perfectly.
    

if __name__ == "__main__":
    main()