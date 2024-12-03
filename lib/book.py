#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title  # Title is always a string
        self.page_count = page_count  # Calls the setter to validate page_count

    # Page count getter
    def get_page_count(self):
        return self._page_count

    # Page count setter
    def set_page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    # Define property for page_count
    page_count = property(get_page_count, set_page_count)

    # Method to simulate turning the page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
