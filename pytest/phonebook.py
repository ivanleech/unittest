import os

class Phonebook:
    def __init__(self, cache_dir):
        self.numbers = {}
        self.filename = os.path.join(cache_dir, "phonebook.txt")
        self.cach = open(self.filename, "w")

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]