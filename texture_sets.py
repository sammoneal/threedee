from textures import bw_image, mono_image, color_image

MONO_COLORS = ('blue','lime','magenta','cyan','gold','red','gray')
POWERS_OF_TWO = (2**i for i in range(3,10))

def mono_set(resolutions=None, colors=None):
    if not resolutions:
        resolutions = POWERS_OF_TWO
    if not colors:
        colors = MONO_COLORS
    for item in zip(resolutions, colors):
        texture = mono_image(item[0], item[1])
        texture.show()

def color_set(resolutions=None):
    if not resolutions:
        resolutions = POWERS_OF_TWO
    for res in POWERS_OF_TWO:
        im = color_image(res)
        im.show()

if __name__ == '__main__':
    mono_set()
