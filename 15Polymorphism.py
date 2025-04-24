class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} makes a general movement.")

class Dog(Animal):
    def move(self):
        print(f"{self.name} runs.")

class Bird(Animal):
    def move(self):
        print(f"{self.name} flies.")

class Fish(Animal):
    def move(self):
        print(f"{self.name} swims.")

# Creating a list of different animal objects
animals = [Dog("Buddy"), Bird("Tweety"), Fish("Goldie")]

# Calling the move() method on each animal
print("\n--- Animal Movements ---")
for animal in animals:
    animal.move()