#Colton Swartwoudt
#Edge Detection and BW
#The purpose of this exercise was to determine whether
#or not converting an image to BW from RGB
#would effect the edge detection filter.

import PIL
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
import numpy as np

def main():
    print("a")
    mech = Image.open("Mech.png")
    mechWithEdges = mech.filter(ImageFilter.FIND_EDGES)
    mechGreyscale = ImageOps.grayscale(mech)
    mechGreyscale = mechGreyscale.filter(ImageFilter.FIND_EDGES)
    #mechWithEdges = mechWithEdges.filter(ImageFilter.BLUR)
    #mech.show()
    mechWithEdges.show()
    mechGreyscale.show()

#Yes, it effects the end result.
#Generally it still does a pretty good job,
#however it does lose out on a few
#places here and there.


if __name__ == "__main__":
    main()