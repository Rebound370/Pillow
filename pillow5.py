#Colton Swartwoudt
#Transparency Masking with ImageDrawing
#The purpose of this exercise is to create a polygonal
#mask using the ImageDraw module, then to use it on another
#image. Eventually, this will be overlayed on top of a filtered
#image to create an effect of normal in the middle, but filtered
#on the edges.

import numpy as np
import PIL
from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageChops

def main():
    print("a")
    im1 = Image.open("Mech.png")
    im1 = ImageOps.grayscale(im1)
    im1 = im1.filter(ImageFilter.BLUR)
    im1 = im1.convert("RGB")
    width = im1.size[0]
    height = im1.size[1]
    blankSet = np.zeros( (height, width) )
    mask = Image.fromarray(blankSet, "RGBA")
    ImageDrawer = ImageDraw.Draw(mask)
    im2 = Image.open("Mech.png")
    im2 = im2.filter(ImageFilter.FIND_EDGES)
    im2 = im2.convert("RGB")

    ImageDrawer.ellipse((width / 6, height / 6) + (5 * width / 6, 5 * height / 6), fill = "black", outline = "black")
    im3 = Image.composite(im2, im1, mask)
    im1.save("pillow5Layer1.png")
    im2.save("pillow5Layer2.png")
    mask.save("pillow5Mask.png")
    im3.save("pillow5Composite.png")

    #This one relied heavily on my previous knowledge accrued from the other four
    #exercises, but still used the composite() function, which was unfamiliar.
    #Overall it went fairly smoothly, but there were a few stumbling blocks.
    #Width and Height of Image.size() and np.zeros are switched. When I went to generate the
    #mask, it generated with the width and height swapped. Beyond that, for the effect I
    #desired, I actually ended up needing to switch the order of im1 and im2 in the composite function.
    


if __name__ == "__main__":
    main()