class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

p = Point(3, 5)

print(p)       # Calls __str__() -> Output: Point(3, 5)
str(p)         # Calls __str__() -> Output: 'Point(3, 5)'
p              # Calls __repr__() -> Output: Point(x=3, y=5)
repr(p)        # Calls __repr__() -> Output: 'Point(x=3, y=5)'
