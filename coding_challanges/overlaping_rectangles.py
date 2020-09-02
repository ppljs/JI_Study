class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

def calculate_overlaping_area(rect1, rect2):
    sorted_xs = sorted([rect1.x1, rect1.x2, rect2.x1, rect2.x2])
    sorted_ys = sorted([rect1.y1, rect1.y2, rect2.y1, rect2.y2])
    return (sorted_xs[2]-sorted_xs[1]) * (sorted_ys[2]-sorted_ys[1])


rect1 = Rectangle(1,1,2,2)
rect2 = Rectangle(1.5,1.5,2.5,2.5)

print(calculate_overlaping_area(rect1, rect2))
