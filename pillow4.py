#Colton Swartwoudt
#Advanced Composite Pictures
#The purpose of this exercise was to
#learn how to draw onto a transparent background,
#then to use that to create a composite with
#another picture.

import numpy as np
import PIL
from PIL import Image, ImageDraw, ImageChops

HEIGHT = 500
WIDTH = 500

def main():
    print("a")
    blankSet = np.zeros( (WIDTH, HEIGHT))
    im1 = Image.fromarray(blankSet, "RGBA")
    im2 = Image.fromarray(blankSet, "RGBA")
    imageDrawer1 = ImageDraw.Draw(im1)
    imageDrawer2 = ImageDraw.Draw(im2)

    imageDrawer1.rectangle((25, 25) + (475, 475), fill = "green", outline = "black", width = 5)
    im1.save("pillow4Green.png")
    im1.show()
    imageDrawer2.rectangle((200, 200) + (300, 300), fill = "blue", outline = "black", width = 5)
    im2.show()
    im2.save("pillow4Blue.png")
    im3 = ImageChops.add(im1, im2)
    im3.show()
    im3.save("pillow4Add.png")
    im4 = ImageChops.blend(im1, im2, 0.5)
    im4.show()
    im4.save("pillow4Blend.png")

    #Once I came up with the idea to create a transparent array and then draw on top of that,
    #it actually went incredibly smoothly. Initially I thought ImageChops.blend() would
    #produce a nicer image, but it added transparency to both instead of using one
    #as a base and transparently adding the other on top of it.
    #ImageChops.add() turned out looking much nicer, combining the green and the blue
    #to make a cyan in the middle. The one quirk is that it appears to lose the black outline
    #of the inner square during the ImageChops.add(), but that's a minor detail.

if __name__ == "__main__":
    main()