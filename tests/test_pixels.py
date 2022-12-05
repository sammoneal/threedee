from pixels import scale_color
from PIL import ImageColor

def test_scale_color():
    my_color = ImageColor.getrgb('blue')

    assert scale_color(my_color, 0) != (0,0,0)
    assert scale_color(my_color, 1) != (255,255,255)
    assert scale_color(my_color, 0.5) == my_color

    assert my_color > scale_color(my_color, 0.4)
    assert my_color < scale_color(my_color, 0.6)

    my_color = ImageColor.getrgb('orange')
    assert scale_color(my_color, 0) != (0,0,0)
    assert scale_color(my_color, 1) != (255,255,255)

    assert scale_color(my_color, 0.5) == my_color
    assert my_color > scale_color(my_color, 0.4)
    assert my_color < scale_color(my_color, 0.6)