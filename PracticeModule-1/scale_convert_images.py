#!/usr/bin/python
import os, sys
from PIL import Image

source = './Images/'
destination = './ConvertedImages/'

for infile in os.listdir(source):
    file, ext = os.path.splitext(infile)
    outfile = file + ".jpeg"
    if infile != outfile:
        try:
            with Image.open(source + infile) as im:
                im.rotate(90).resize((128, 128)).convert("RGB").save(destination + outfile)
        except OSError as e:
            print("Failed to convert !", infile, getattr(e, 'message', str(e)))

