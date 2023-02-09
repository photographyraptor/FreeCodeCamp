class Rectangle:
    def __init__(self, width:int, height:int=None):
        self.width = width
        self.height = height if height is not None else width

    def __str__(self):
        if (self.height == self.width):
            return "Square(side=" + str(self.height) + ")"
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")" 
    
    def get_area(self):
        return self.width * self.height
    
    def set_width(self, width):
        if (self.height == self.width):
            self.height = width
        self.width = width
    
    def set_height(self, height):
        if (self.width == self.height):
            self.width = height
        self.height = height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if (self.height > 50 or self.width > 50):
            return "Too big for picture."
        lines = []
        for _i in range(0, self.height):
            lines.append(("*" * self.width))        
        return "\n".join(lines) + "\n"

    def get_amount_inside(self, to):
        left = int(self.width / to.width)
        right = int(self.height / to.height)
        return left * right


class Square(Rectangle):
    def set_side(self, side):
        self.set_height(side)
        self.set_width(side)
