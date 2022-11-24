import os
from PIL import Image

files = os.listdir('temp')
files = sorted(files, key=lambda file: os.path.getctime(os.path.join('temp', file)))
frames = []
for img in files:
    frames.append(Image.open(os.path.join('temp', img)))

frames[0].save('temp.gif', save_all = True, append_images = frames[1:], duration =1000, loop=100)