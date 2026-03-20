#convert all the .svg files in the current directory to .png files with 600dpi
import os
from PIL import Image
for file in os.listdir():
    if file.endswith(".svg"):
        img = Image.open(file)
        img.save(file.replace(".svg", ".png"), dpi=(600, 600))
        