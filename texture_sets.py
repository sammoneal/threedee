import os
from textures import bw_image, mono_image, color_image
from utils import powers_of_two

MONO_COLORS = ('cyan','lime','magenta','blue','gold','darkred','gray')
PREFERRED_COLORS = ('navy','teal','purple','maroon','olive','green','gray')

def mono_set(resolutions=None, colors=None):
    if resolutions is None:
        resolutions = powers_of_two(start=3)
    if colors is None:
        colors = PREFERRED_COLORS
    for item in zip(resolutions, colors):
        im = mono_image(item[0], item[1])
        location = os.path.join(os.path.dirname(__file__), 'output','mono')
        location = os.path.join(location,'test_'+str(item[0])+'.png')
        im.save(location,"PNG")
        print('Saved: ' + location)

def color_set(resolutions=None):
    if resolutions is None:
        resolutions = powers_of_two(3,10)
    for res in resolutions:
        im = color_image(res)
        location = os.path.join(os.path.dirname(__file__), 'output','color')
        location = os.path.join(location,'test_'+str(res)+'.png')
        im.save(location,"PNG")
        print('Saved: ' + location)


if __name__ == '__main__':
    mono_set()
    color_set()
