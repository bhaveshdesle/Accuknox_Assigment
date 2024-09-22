# rectangle.py

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage
if __name__ == "__main__":
    rect = Rectangle(10, 5)

    # Iterate over the instance
    for dimension in rect:
        print(dimension)
