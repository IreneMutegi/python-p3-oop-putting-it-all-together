#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand  # Brand is a simple attribute
        self.size = size  # Calls the setter for validation

    # Getter for size
    def get_size(self):
        return self._size

    # Setter for size with validation
    def set_size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    # Define property for size
    size = property(get_size, set_size)

    # Method to cobble (repair) the shoe
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"  # Set condition to "New"
