from Shape import Shape, Circle, Triangle
from Test import TestShapes

def get_area(shape: Shape):
    return shape.area()

def main():
    circle = Circle(4)
    triangle = Triangle(20, 45, 26)
    print(get_area(circle))
    print(get_area(triangle))
    if triangle.is_right_angled():
        print("Triangle is right-angled")
    else:
        print("Triangle is not right-angled")


if __name__ == "__main__":
    main()