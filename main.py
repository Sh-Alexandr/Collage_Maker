from PIL import Image
from numpy import asarray
import numpy as np
def collage_maker(image1, image2, name):
    image11 = Image.open(image1)
    data1 = asarray(image11)
    image22 = Image.open(image2)
    data2 = asarray(image22)
    collage = np.vstack((data1, data2))
    image = Image.fromarray(collage)
    image.save(name)

# To Run The Above Function
collage_maker("image1.png", "image2.png", "new.png")

