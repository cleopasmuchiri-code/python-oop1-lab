#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

        if not isinstance(self.page_count, int): 
            raise ValueError("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
        