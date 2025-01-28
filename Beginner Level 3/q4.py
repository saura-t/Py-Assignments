class Shape:
    def area(self):
        return 0  # Default area for any shape is 0

class Square(Shape):
    def __init__(self, l):
        self.l = l
    
    def area(self):
        return pow(self.l, 2)

if __name__ == "__main__":
    try:
        l = int(input("Enter length of side: "))
        sh = Shape()
        sq = Square(l)
        print(f"Calling Shape: {sh.area()}")
        print(f"Calling Square: {sq.area()}")
    except Exception as e:
        print(e)