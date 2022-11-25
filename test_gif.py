import os
from PIL import Image

files = os.listdir('temp')
files = sorted(files, key=lambda file: os.path.getctime(os.path.join('temp', file)))
frames = []
for img in files:
    img = Image.open(os.path.join('temp', img))
    img = img.resize((img.size[0]//2, img.size[1]//2), Image.CUBIC)
    frames.append(img)

frames[0].save('temp.gif', save_all = True, append_images = frames[1:], duration =800, loop=10)