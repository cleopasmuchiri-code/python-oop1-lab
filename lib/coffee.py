#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

        if self.size not in ["Small", "Medium", "Large"]:
            raise ValueError("size must be Small, Medium, or Large")

    def tip(self):
        self.price += 1
        print("This coffee is great, here’s a tip!")