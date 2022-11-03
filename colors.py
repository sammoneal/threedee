class Color():

    def __init__(self, red=0, blue=0, green=0) -> None:
        self.red = red
        self.blue = blue
        self.green = green

    def __iter__(self):
        return (component for component in (self.red, self.blue, self.green))

    @property
    def hexcode(self):
        code = ''
        for item in self:
            digits = hex(item)[2:]
            digits = digits.zfill(2)
            code += digits
        return code

if __name__ == "__main__":
    my_color = Color(red=255,blue=179,green=8)
    print(my_color.red,my_color.blue,my_color.green)
    for item in my_color:
        print(item)
    print(my_color.hexcode)
