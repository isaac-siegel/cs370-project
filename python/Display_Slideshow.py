import pylab as pl
import os

def display():
    os.chdir("steps")

    files = [f for f in os.listdir('.') if f[-3:] == 'png']

    img = None
    for f in files:
        im=pl.imread(f)
        if img is None:
            img = pl.imshow(im)
        else:
            img.set_data(im)
        pl.pause(1)
        pl.draw()

display()

